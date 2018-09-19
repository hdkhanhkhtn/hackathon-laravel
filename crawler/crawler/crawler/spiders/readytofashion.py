# -*- coding: utf-8 -*-
import scrapy
import logging
import re
from datetime import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import BaseSpider, CrawlSpider, Rule
from scrapy.selector import Selector
from crawler.database.model import NewsItem, Categories
from crawler.database.settings import session
# from base_scraper import BaseScraperz

logger = logging.getLogger(__name__)

class ReadytofashionSpider(CrawlSpider):
    name = 'readytofashion'
    allowed_domains = ['www.readytofashion.jp']
    start_urls = ['https://www.readytofashion.jp/mag/news/page/1']
    category = session.query(Categories).filter(Categories.id == 1).one() ## FASHION

    rules = (
        Rule(LinkExtractor(allow=r"/mag/news/page/[0-5]", unique=True), callback="parse_item", follow=True),
    )
    

    def parse_item(self, response):
        logger.info('Hi, this is an item page! %s', response.url)

        items = []
        listNews = response.xpath('//*[@id="kad-blog-grid"]/div')
        for news in listNews:
            detail_url = news.css('.postcontent>header>a::attr(href)').extract_first()
            yield scrapy.Request(detail_url, callback=self.parse_content)

        # next_page = response.xpath('//*[contains(@class,"next") and contains(@class,"page-numbers")]/@href').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse_item)


    def parse_content(self, response):
        logger.info('Hi, this is an item content! %s', response.url)

        content = self.preProcessContent(response.css('.entry-content'))
        post_date_str = response.css('span.postday::text').extract_first()
        post_date = datetime.now()
        if post_date_str != '':
            post_date = datetime.strptime(post_date_str, '%Y-%m-%d')
        yield {
            'url' : response.url,
            'title' : response.css('h2.entry-title::text').extract_first(),
            'thumbnail' : response.css('.entry-content>p:first-child>img::attr(data-src)').extract_first(default=''),
            'content' : content,
            'site_name' : self.name,
            'category' : self.category,
            'post_date' : post_date,
            'archive_type' : 0,
        }

    def preProcessContent(self, content):
        _image = content.css('p:first-child>img')
        if _image is not None:
            _image = content.css('p:first-child').extract_first()

        _del1 = content.css('.card-area').extract_first()
        _del2 = content.css('.button-area-second').extract_first()
        _del3 = content.css('.card-area-second').extract_first()
        _del4 = content.css('.button-area').extract_first()
        _del5 = content.css('.rp4wp-related-posts').extract_first()

        content = content.extract_first()
        content = content.replace(_image, '')
        content = content.replace(_del1, '')
        content = content.replace(_del2, '')
        content = content.replace(_del3, '')
        content = content.replace(_del4, '')
        content = content.replace(_del5, '')

        return content


