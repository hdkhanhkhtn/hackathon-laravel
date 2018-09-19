# -*- coding: utf8 -*-
import scrapy
import logging
import re
from datetime import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import BaseSpider, CrawlSpider, Rule
from scrapy.selector import Selector
from crawler.database.model import NewsItem, Categories
from crawler.database.settings import session


class DetailScraper(scrapy.Spider):
    name = None
    urls = []
    xpaths = {}
    _url = ""
    _title = ""
    _thumbnail = ""
    _content = ""
    _site_name = ""
    _category = ""
    _post_date = datetime.now()
    _archive_type = 0

    def start_request(self):
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_artilce)

    def parse_artilce(self, response):
        # artilce = ScraperItem()
        self._url = response.url
        self._post_date = datetime.now()

        artilce = {
            'url' : response.url,
            'title' : self._title,
            'thumbnail' : self._thumbnail,
            'content' : self._content,
            'site_name' : self._site_name,
            'category' : self._category,
            'post_date' : datetime.now(),
            'archive_type' : self._archive_type,
        }

        for key in self.xpaths.keys:
            self.artilce[key] = response.xpath(self.xpaths[key]).extract()[0].encode('utf-8').strip()
        yield artilce