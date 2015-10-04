import redis
import run
import os
import time
from queue import RedisQueue

redis_url = os.getenv('REDISTOGO_URL')
# r = redis.Redis.from_url(redis_url)
scraper_q = RedisQueue('scrapers', redis_url)

while True:
    print 'checking work queue'
    message = scraper_q.dequeue()
    print message
    if message[1] == 'CRAWL ALL SPIDERS':
        run.crawl_all()
        print 'DONE CRAWLING'
    time.sleep(2)
