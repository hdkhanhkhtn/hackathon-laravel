# -*- coding: utf-8 -*-
"""
How to run scrapers from a script
"""
from spiders.readytofashion import ReadytofashionSpider

# scrapy api
from scrapy import signals, log
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings


# list of crawlers
TO_CRAWL = [ReadytofashionSpider]

# list of crawlers that are running 
RUNNING_CRAWLERS = []

def spider_closing(spider):
    """Activates on spider closed signal"""
    log.msg("Spider closed: %s" % spider, level=log.INFO)
    RUNNING_CRAWLERS.remove(spider)
    if not RUNNING_CRAWLERS:
        reactor.stop()

log.start(loglevel=log.DEBUG)
for spider in TO_CRAWL:
    settings = Settings()

    # crawl responsibly
    settings.set("USER_AGENT", "Khanhhd (+http://blog.hdkhanh.com)")

    # Add to items pipelines
    settings.set("ITEM_PIPELINES", {'crawler.pipelines.CrawlerPipeline': 300})

    crawler = Crawler(settings)
    crawler_obj = spider()
    RUNNING_CRAWLERS.append(crawler_obj)

    # stop reactor when spider closes
    crawler.signals.connect(spider_closing, signal=signals.spider_closed)
    crawler.configure()
    crawler.crawl(crawler_obj)
    crawler.start()

# blocks process so always keep as the last statement
reactor.run()
