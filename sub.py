import redis
import run
import os

redis_url = os.getenv('REDISTOGO_URL')

r = redis.StrictRedis.from_url(redis_url)
channel = r.pubsub()
channel.subscribe('scrapers')

while True:
    message = channel.get_message()
    if message:
        print message['data']
        if message['data'] == 'CRAWL ALL SPIDERS':
            run.crawl_all()
            print 'DONE CRAWLING'
