# -*- coding: utf-8 -*-

# えすきゅーえるあるけみー
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base, DeferredReflection

# db settings
dbhost = '172.19.0.3' #os.environ['DB_HOST']
dbname = 'hdk_news' #os.environ['MYSQL_DATABASE']
dbuser = 'khanhhd' #os.environ['MYSQL_USER']
dbpass = 'khanhhd' #os.environ['MYSQL_PASSWORD']

connection_str = "mysql+pymysql://%s:%s@%s/%s" % (dbuser, dbpass, dbhost, dbname)
engine = create_engine(connection_str,
                            encoding='utf-8', 
                            echo=True)
session_factory = sessionmaker(autocommit=False,
						autoflush=False,
                        bind=engine)
 
# Bind the sessionmaker to engine
session_factory.configure(bind=engine)

## If the session objects are retrieved from a scoped_session object, however, then we don't have such an issue since the scoped_session object maintains a registry for the same session object.
# https://www.pythoncentral.io/understanding-python-sqlalchemy-session/
session = scoped_session(session_factory)
# DeclarativeBase = declarative_base(cls=DeferredReflection)
