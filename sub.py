import redis
import run
import os
import time
from queue import RedisQueue

redis_url = os.getenv('REDISTOGO_URL')
scraper_q = RedisQueue('scrapers', redis_url)

# Listens for message 'CRAWL ALL SPIDERS' on Redis queue at key 'scrapers'

while True:
    print 'checking work queue'
    message = scraper_q.dequeue()
    print message
    if message[1] == 'CRAWL ALL SPIDERS':
        run.crawl_all()
        print 'DONE CRAWLING'
    if message[1] == 'PRINT DIRS':
        run.print_dirs()
    time.sleep(2)
