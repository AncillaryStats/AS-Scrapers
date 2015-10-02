from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose
from scrapy.utils.response import get_base_url
from urlparse import urljoin
from scrapy.http import Request

from espn_scraper.items import NFL_Team_2015

class EspnSpider(Spider):
    name = 'nfl_team_info'
    allowed_domains = ['espn.com', 'espn.go.com']
    start_urls = ['http://espn.go.com/nfl/teams']

    # item_fields = {
    #     'division' : '//*[@id="sub-branding"]/div[2]/text()',
    #     'team_name' : '//*[@id="sub-branding"]/h2/a/b/text()'
    # }

    # Follows all links to nfl teams' depth charts
    def parse(self, response):
        base_url = get_base_url(response)

        depth_charts = response.xpath('//a[text()="Depth Chart"]/@href').extract()
        for depth_chart in depth_charts:
            link = urljoin(base_url, depth_chart)
            yield Request(link, callback = self.parse_depth_chart)

    # Follows all links for individual QBs, WRs, TEs, RBs, and FBs on team depth chart
    def parse_depth_chart(self, response):


        loader = ItemLoader(item=NFL_Team_2015(), response=response)

        loader.default_input_processor = MapCompose(unicode.strip)
        loader.default_output_processor = Join()

        loader.add_xpath('division', '//*[@id="sub-branding"]/div[2]/text()')
        loader.add_xpath('name', '//*[@id="sub-branding"]/h2/a/b/text()')

        yield loader.load_item() 


