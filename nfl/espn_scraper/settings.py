
SPIDER_MODULES = ['espn_scraper.spiders']

# DATABASE = {
#     'drivername': 'postgres',
#     'host': 'localhost',
#     'port': '5432',
#     'username': 'arosenberg',
#     'database': 'nfl_test_2'
# }

DATABASE = {
    'drivername': 'postgres',
    'host': 'ec2-54-163-228-109.compute-1.amazonaws.com',
    'port': '5432',
    'username': 'npapimuvhzikjb',
    'password': 'vdt-V65Njuzh1pr3d92byTAnFz',
    'database': 'dak2n8qnpioi1g'
}

ITEM_PIPELINES = {
    'espn_scraper.pipelines.NFL_Team_Info_2015_Pipeline': 100,
    'espn_scraper.pipelines.NFL_Player_2015_Pipeline': 200,
    'espn_scraper.pipelines.NFL_QB_Stats_2015_Pipeline': 300,
    'espn_scraper.pipelines.NFL_RB_Stats_2015_Pipeline': 400,
    'espn_scraper.pipelines.NFL_WR_Stats_2015_Pipeline': 500,
    'espn_scraper.pipelines.NFL_TE_Stats_2015_Pipeline': 600
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
AUTOTHROTTLE_ENABLED=True
# The initial download delay
AUTOTHROTTLE_START_DELAY=3

DOWNLOAD_DELAY=2

COOKIES_ENABLED=False