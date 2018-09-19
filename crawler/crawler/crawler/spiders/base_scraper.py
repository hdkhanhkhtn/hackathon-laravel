# -*- coding: utf-8 -*-
import scrapy
from crawler.items import NewsItem

# See https://viblo.asia/p/gioi-thieuhuong-dan-ve-crawler-voi-scrapy-framework-phan-3-gDVK2kovZLj
class BaseScraper(scrapy.Spider):
    name = None
    start_urls = []
    xpaths = {}

    def start_request(self):
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        logger.info('Hi, this is an item page! %s', response.url)
        artilce = NewsItem()
        for key in self.xpaths.keys:
            artilce[key] = response.xpath(self.xpaths[key]).extract_first().encode('utf-8').strip()

        return artilce