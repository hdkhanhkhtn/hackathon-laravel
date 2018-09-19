 # -*- coding: utf-8 -*-
import os
import sys
import datetime
from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String, TEXT, DateTime, SMALLINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm.attributes import InstrumentedAttribute
from .settings import *

# DeclarativeBase = declarative_base()
DeclarativeBase = automap_base()
metadata = MetaData(bind=engine)

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)
    # DeclarativeBase.metadata.reflect(engine)
    # DeclarativeBase.prepare(engine)

class Categories(DeclarativeBase):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    slug = Column(String(250))
    name = Column(String(250))
    name_jp = Column(String(250))

class NewsItem(DeclarativeBase):
    __tablename__ = 'newsitem'
    # __table__ = Table("newsitem", metadata, autoload=True, autoload_with=engine)

    def cat_serializer(value):
        return '[RUBY] %s' % str(value)

    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    url = Column(String(250))
    thumbnail = Column(String(250))
    content = Column(TEXT())
    site_name = Column(String(250))
    archive_type = Column(SMALLINT) # 0: news / 1: image
    category = relationship(Categories)
    post_date = Column('post_date', DateTime, default = datetime.datetime.now, nullable=True)
    create_date = Column('create_date', DateTime, default = datetime.datetime.now, onupdate=datetime.datetime.now, nullable=True)

    def __init__(self, id=None, title=None, url=None, thumbnail=None, content=None, site_name=None, archive_type=None, category=None, post_date=None, create_date=None):
        self.id = id
        self.title = title
        self.url = url
        self.thumbnail = thumbnail
        self.content = content
        self.site_name = site_name
        self.archive_type = archive_type
        self.category = category
        self.post_date = post_date
        self.create_date = create_date

    def update(self):
        s = session()
        mapped_values = {}
        for item in NewsItem.__dict__.iteritems():
            field_name = item[0]
            field_type = item[1]
            is_column = isinstance(field_type, InstrumentedAttribute)
            attr = getattr(self, field_name)
            if is_column and attr and field_name != 'category':
                mapped_values[field_name] = attr

        s.query(NewsItem).filter(NewsItem.url == self.url).update(mapped_values)
        s.commit()

    # def __repr__(self):
    #     return "<NewsItem('%s','%s','%s','%s','%s','%s','%s')>" % (self.title, self.url, self.thumbnail, 
    #         self.content, self.site_name, self.archive_type, self.create_date)


# reflect the tables
DeclarativeBase.prepare(engine, reflect=True)
