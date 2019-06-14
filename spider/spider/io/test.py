'''
Created on 2019-06-02

@author: F-Monkey
'''
from scrapy.conf import settings
import redis


def save():
    from spider.io.pojo import User
    obj = User(url='1111', nickName='222', sex='F', head='222')
    from spider.io.DB import session
    from spider.io.DB import engine
    from spider.io.DB import Base
    Base.metadata.create_all(engine)
    session.add(obj)  # @UndefinedVariable
    session.commit()  # @UndefinedVariable


r = redis.Redis(host=settings['REDIS_HOST'], port=settings['REDIS_PORT'])
def redisTest():

    r.lpush('tieba:user_urls','http://tieba.baidu.com/home/main?un=%E8%82%A5%E7%8C%B4%E4%B8%B6&fr=ibaidu&ie=utf-8')

def redisTest2():
    list_ = r.lrange('tieba:user_urls',0,-1)
    print(list_)

def printFloat():
    f = 0.01
    print('%f' %f)

if __name__ == '__main__':
    printFloat()