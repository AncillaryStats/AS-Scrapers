import redis
import run
import os

redis_url = os.environ('REDISTOGO_URL')

r = redis.StrictRedis.from_url(redis_url)
channel = r.pubsub()
channel.subscribe('scrapers')

while True:
    message = channel.get_message()
    if message and message['data'] == 'CRAWL ALL SPIDERS':
        print 'CRAWLING ALL SPIDERS'
        run.crawl_all()
        print 'DONE CRAWLING'
