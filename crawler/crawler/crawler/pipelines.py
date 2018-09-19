# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# Sqlalchemy docs: https://docs.sqlalchemy.org/en/latest/
import os
import logging
from sqlalchemy import (
    create_engine,
    Table,
    Column,
    MetaData,
    Integer,
    Text,
    select
)
from scrapy.exceptions import DropItem
from database.settings import session, engine
from database.model import NewsItem

logger = logging.getLogger(__name__)

class CrawlerPipeline(object):

    def __init__(self):
        self.connection = engine.connect()

    def process_item(self, item, spider):
        """Save items in the database.
        """
        newsitem = NewsItem(**item)
        news_in_db = session.query(NewsItem).filter_by(url = newsitem.url).first()
        if(news_in_db is None):
            try:
                session.add(newsitem)
                session.commit()
            except Exception as e:
                session.rollback()
                raise e
            finally:
                session.close()
        else:
            newsitem.update()
            logger.info("<----------------ALREADY IN------------------>")
            logger.info(news_in_db.title)
            logger.info("<-------------------------------------------->")
        return item
