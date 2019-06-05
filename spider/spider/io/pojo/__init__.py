'''
    POJOS
    create by F-Monkey 2019-06-03

'''
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import INTEGER, String
from spider.io.DB import Base


class User(Base):
    # tableName
    __tablename__ = 'user'
    # columns
    id = Column(u'id', INTEGER, primary_key=True)
    url = Column(u'url', String(250))
    nickName = Column(u'nickName', String(50))
    sex = Column(u'sex', String(1))
    head = Column(u'head', String(250))
    age = Column(u'age', String(10))
    title_count = Column(u'title_count', String(20))
    
    def __repr__(self):
        return "%s" % self.url

class TitleDetail(Base):
    
    __tablename__ = 'title_detail'
    
    id = Column('id',INTEGER,primary_key=True)
    title_url = Column('title_url',String(250))
    content = Column('content',String(5000))
    user_url = Column('user_url',String(250))
    
    def __repr__(self):
        return "%s" % self.content

class Img(Base):
    
    __tablename__ = 'img'
    
    id = Column('id',INTEGER,primary_key=True)
    title_url = Column('title_url',String(250))
    user_url = Column('user_url',String(250))
    # img_url
    img_url = Column('img_url',String(250))
    # img local url ...
    local_url = Column('img_local_url',String(200))


class Title(Base):
    __tablename__ = 'title'
    
    id = Column('id', INTEGER, primary_key=True)
    url = Column('url', String(250))
    title = Column('title', String(100))
    user_url = Column('user_url', String(250))

    def __repr__(self):
        return '%s' % self.title


