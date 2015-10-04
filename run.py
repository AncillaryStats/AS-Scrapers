import datetime
import os

def crawl_spider(spider_name):
    f = open('track_crawlers', 'a')
    f.write('crawling spider %s @ %s\n' % (spider_name, datetime.datetime.now()))
    f.close()
    os.system('scrapy crawl %s' % spider_name)

def crawl_all():
    """Runs all listed scrapy spiders"""
    cwd = os.path.dirname(os.path.realpath(__file__))
    print cwd
    os.chdir(cwd + '/nfl/espn_scraper/')
    new_dir = os.path.dirname(os.path.realpath(__file__))
    print new_dir

    spiders = ['nfl_players', 'nfl_qb_stats', 'nfl_rb_stats', 'nfl_wr_stats', 'nfl_te_stats', 'nfl_team_info']

    for spider in spiders:
       crawl_spider(spider)

    f = open('track_crawlers.txt', 'a')
    f.write('DONE CRAWLING @ %s\n', datetime.datetime.now())
    f.close()
