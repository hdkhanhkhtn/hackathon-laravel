# -*- coding: utf-8 -*-
import scrapy


class SpiderBasicSpider(scrapy.Spider):
    name = 'spider_basic'
    allowed_domains = ['scrapy.org']
    start_urls = ['http://scrapy.org/']

    def parse(self, response):
        pass
