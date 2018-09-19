# -*- coding: utf-8 -*-
# https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Spider.parse
# scrapy crawl quotes -o quotes-humor.json -a tag=humor
# scrapy crawl quotes -o quotes-humor.json -a http_user=myuser -a http_pass=mypassword -a user_agent=mybot
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # def __init__(self, category=None, *args, **kwargs):
    #     super(MySpider, self).__init__(*args, **kwargs)
    #     self.start_urls = ['http://www.example.com/categories/%s' % category]


    # start_urls = [
    #     'http://quotes.toscrape.com/page/1/',
    # ]

    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    
    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    # parse() is Scrapy’s default callback method, which is called for requests without an explicitly assigned callback.
    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse) ## Unlike scrapy.Request, response.follow supports relative URLs directly

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse) ## Can also pass a selector to response.follow instead of a string; this selector should extract necessary attributes:

        # for a in response.css('li.next a'):
        #     yield response.follow(a, callback=self.parse)
        #     

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }
    



