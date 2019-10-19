'''
Created on 2019-06-02

@author: F-Monkey
'''
from sqlalchemy.engine import create_engine
from spider.io import settings
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative.api import declarative_base
import os

#!/usr/bin/python3
'''
    https://www.cnblogs.com/gispathfinder/p/5787313.html
    echo : log sql
'''
engine = create_engine(settings.DB_URL, max_overflow=settings.DB_MAX_OVERFLOW, echo=True)

Session = sessionmaker(bind=engine)

session = Session()

# pojos parent
Base = declarative_base()

if __name__ == '__main__':
    print(os.path.dirname(settings.__file__))
