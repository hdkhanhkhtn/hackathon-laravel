# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# v

import scrapy


class CategoryItem(scrapy.Item):
	cat_name = scrapy.Field()
	# cat_parent = CategoryItem

class NewsItem(scrapy.Item):
	def cat_serializer(value):
		return '[RUBY] %s' % str(value)

	title = scrapy.Field()
	url = scrapy.Field()
	thumbnail = scrapy.Field()
	content = scrapy.Field()
	site_name = scrapy.Field()
	create_date = scrapy.Field(serializer=str)
	pass

class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    description = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    publish_date = scrapy.Field()