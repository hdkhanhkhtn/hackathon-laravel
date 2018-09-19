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

class FashionpressMaster(scrapy.Spider):
    site_name = 'www.fashion-press.net'

    def parse_content(self, response):
        logger.info('Hi, this is an item content! %s', response.url)
        thumbnail = response.meta['thumbnail']
        if thumbnail is None:
            thumbnail = response.css('#news.feature_news img::attr(src)').extract_first()

        post_date_str = response.css('.footer_caption span:first-child::text').extract_first()
        post_date = datetime.now()
        if post_date_str != '':
            post_date = datetime.strptime(post_date_str.split(' ')[0], '%Y-%m-%d')

        yield {
            'url' : response.url,
            'title' : response.css('.fp_content .h1_wrapper h1::text').extract_first(),
            'thumbnail' : thumbnail,
            'content' : response.css('#news').extract_first(),
            'site_name' : self.site_name,
            'category' : self.category,
            'post_date' : post_date,
            'archive_type' : 0,
        }

class FashionpressSpider(FashionpressMaster):
    name = 'fashionpress'
    site_name = 'www.fashion-press.net'
    rootDomain = 'https://www.fashion-press.net'
    allowed_domains = ['www.fashion-press.net']
    start_urls = ['https://www.fashion-press.net/news/search/fashion?page=1']
    category = session.query(Categories).filter(Categories.id == 1).one() ## FASHION

    def parse(self, response):
        logger.info('Hi, this is an item page! %s', response.url)

        listNews = response.css('.fp_tile>div.fp_media_tile.news_media')
        for news in listNews:
            detail_url = self.rootDomain + news.css('div.fp_media_tile.news_media>a::attr(href)').extract_first()
            thumbnail = self.rootDomain + news.css('div.fp_media_tile.news_media img::attr(data-original)').extract_first()
            yield response.follow(detail_url, callback=self.parse_content, meta={'thumbnail': thumbnail})

        next_page = response.css('.pagination-link[rel="next"]::attr(href)').extract_first()
        logger.info("========================================")
        logger.info(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            # import re
            # matches = re.search("https://www.fashion-press.net/news/search/fashion\?page=([\d])", next_page)
            # if matches != None and matches.group(1) < 50:
            #     yield response.follow(next_page, callback=self.parse)
        

class FashionpressGoumetSpider(FashionpressMaster):
    name = 'fashionpress.goumet'
    site_name = 'www.fashion-press.net'
    rootDomain = 'https://www.fashion-press.net'
    allowed_domains = ['www.fashion-press.net']
    start_urls = ['https://www.fashion-press.net/news/search/gourmet?page=1']
    category = session.query(Categories).filter(Categories.id == 4).one() ## FASHION

    def parse(self, response):
        logger.info('Hi, this is an item page! %s', response.url)

        listNews = response.css('.fp_tile>div.fp_media_tile.news_media')
        for news in listNews:
            detail_url = self.rootDomain + news.css('div.fp_media_tile.news_media>a::attr(href)').extract_first()
            thumbnail = self.rootDomain + news.css('div.fp_media_tile.news_media img::attr(data-original)').extract_first()
            yield response.follow(detail_url, callback=self.parse_content, meta={'thumbnail': thumbnail})

        next_page = response.css('.pagination-link[rel="next"]::attr(href)').extract_first()
        logger.info("========================================")
        logger.info(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

