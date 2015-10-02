from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from scrapy.utils.response import get_base_url
from urlparse import urljoin
from scrapy.http import Request
import json
import datetime

from espn_scraper.items import NFL_WR_Game_2015

class EspnSpider(Spider):
    name = 'nfl_wr_stats'
    allowed_domains = ['espn.com', 'espn.go.com']
    start_urls = ['http://espn.go.com/nfl/teams']

    # start_urls = ['http://espn.go.com/nfl/player/gamelog/_/id/16763/jordan-matthews',
    #               'http://espn.go.com/nfl/player/gamelog/_/id/13934/antonio-brown',
    #               ]

    # Follows all links to nfl teams' depth charts
    def parse(self, response):
        base_url = get_base_url(response)

        depth_charts = response.xpath('//a[text()="Depth Chart"]/@href').extract()
        for depth_chart in depth_charts:
            link = urljoin(base_url, depth_chart)
            yield Request(link, callback = self.parse_depth_chart)

    # Follows all links for individual QBs, WRs, TEs, RBs, and FBs on team depth chart
    def parse_depth_chart(self, response):

        rows = response.xpath('//*[@id="my-teams-table"]/div[4]/div[1]/table/tr')
        for row in rows:
            players = row.xpath('td/strong/a | td/a')
            # players = row.xpath('td//a')

            names = players.xpath('text()').extract()
            links = players.xpath('@href').extract()
            cols = row.xpath('td')
            position = cols[0].xpath('text()').extract()[0]

            if position == 'WR':
                if len(links) > 0:
                    for link, name in zip(links, names):
                        yield Request(link, callback = self.go_to_player)

    # Follows link to player's game long for most recent year
    # TODO: add argument for year?
    def go_to_player(self, response):
        game_log = response.xpath('//*[@id="content"]/div[6]/div[1]/div[2]/div/p/a/@href').extract()

        if game_log:
            game_log = game_log[0]
            print('\n')
            base_url = get_base_url(response)
            absolute_path = urljoin(base_url, game_log)
            print('going to game log', absolute_path)
            yield Request(absolute_path, callback = self.parse_game_log)

    # Convert table of game stats into scrapy items to be sent to pipeline for db storage
    def parse_game_log(self, response):
        games_table = []

         # If default selector returns empty, try second selector
        rows = response.xpath('//*[@id="content"]/div[6]/div[1]/div/div[4]/div/table[1]/tr')
        if not bool(rows):
            rows = response.xpath('//*[@id="content"]/div[6]/div[1]/div/div[3]/div/table/tr')

        # Build up game stats table to be turned into scrapy items
        for row in rows:

            game_row = []
            for col in row.xpath('td'):

                opponent = col.xpath('ul/li[3]/a/text()').extract()
                game_result = col.xpath('a/text()').extract()
                other_value = col.xpath('text()').extract()

                if opponent:
                    game_row.append(opponent[0])
                elif game_result:
                    game_row.append(game_result[0])
                else:
                    game_row.append(other_value[0])

            games_table.append(game_row)

        # print json.dumps(games_table, indent=1)

        # Load game stat rows into scrapy items
        for game_row in games_table:
            print(game_row)
            
            # Initialize WR game item to be loaded
            loader = ItemLoader(item=NFL_WR_Game_2015(), response=response)

            # Set default output process to take first item from selector
            loader.default_output_processor = TakeFirst()

            # Add player name
            loader.add_xpath('player_name', '//*[@id="content"]/div[3]/div[2]/h1/text()', MapCompose(unicode.strip))

            # Handle regular season totals row
            if game_row[0] == 'REGULAR SEASON STATS':
                loader.add_value('is_season_totals', True)
                loader.add_value('date', None)
                loader.add_value('opponent', None)
                loader.add_value('result', None)

                loader.add_value('receptions', int(game_row[1]))
                loader.add_value('targets', int(game_row[2]))
                loader.add_value('rec_yards', int(game_row[3]))
                loader.add_value('avg_yards_per_rec', float(game_row[4]))
                loader.add_value('longest_rec', int(game_row[5]))
                loader.add_value('rec_tds', int(game_row[6]))
                loader.add_value('rush_attempts', int(game_row[7]))
                loader.add_value('rush_yards', int(game_row[8]))
                loader.add_value('avg_yards_per_rush', float(game_row[9]))
                loader.add_value('longest_rush', int(game_row[10]))
                loader.add_value('rush_tds', int(game_row[10]))
                loader.add_value('fumbles', int(game_row[11]))
                loader.add_value('fumbles_lost', int(game_row[12]))

                yield loader.load_item()

            # Handle regular season individual game row (ignoes two header rows)
            elif game_row[0] != '2015 REGULAR SEASON GAME LOG' and game_row[0] != 'DATE':

                # Parse date from string containing day of the week and date
                day_and_date = game_row[0]
                date = day_and_date.split()[1] + '/15'

                loader.add_value('is_season_totals', False)
                loader.add_value('date', date)
                loader.add_value('opponent', game_row[1])
                loader.add_value('result', game_row[2])

                loader.add_value('receptions', int(game_row[3]))
                loader.add_value('targets', int(game_row[4]))
                loader.add_value('rec_yards', int(game_row[5]))
                loader.add_value('avg_yards_per_rec', float(game_row[6]))
                loader.add_value('longest_rec', int(game_row[7]))
                loader.add_value('rec_tds', int(game_row[8]))
                loader.add_value('rush_attempts', int(game_row[9]))
                loader.add_value('rush_yards', int(game_row[10]))
                loader.add_value('avg_yards_per_rush', float(game_row[11]))
                loader.add_value('longest_rush', int(game_row[12]))
                loader.add_value('rush_tds', int(game_row[13]))
                loader.add_value('fumbles', int(game_row[14]))
                loader.add_value('fumbles_lost', int(game_row[15]))

                yield loader.load_item()


        # print json.dumps(games_table, indent=1)


