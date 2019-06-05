# -*- coding: utf-8 -*-
import redis
from scrapy.conf import settings
from pybloom_live import BloomFilter

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderPipeline(object):

    def process_item(self, item, spider):
        return item


from spider.io.pojo import User, Title, TitleDetail, Img
from spider.io.DB import session
from spider.io.DB import engine
from spider.io.DB import Base

Base.metadata.create_all(engine)

# redis
r = redis.Redis(host=settings['REDIS_HOST'], port=settings['REDIS_PORT'])


def processUserURL(url):
    return url.split('&ie=')[0]


user_bloomFilter = BloomFilter(capacity=2 << 15, error_rate=0.01)
img_bloomFilter = BloomFilter(capacity=2 << 15, error_rate=0.01)


class TiebaPipeline(object):
    
    def process_item(self, item, spider):
        user_url = processUserURL(item['user_url'])
        t = Title(url=item['url'], title=item['title'], user_url=user_url)
        if 'home/main?un' in user_url and user_url not in user_bloomFilter:
            user_bloomFilter.add(user_url)
            r.lpush('tieba:user_urls', user_url)
        else:
            print('unsupport user_url:%s' % user_url)
        r.lpush('tieba:title_urls', item['url'])
        session.add(t)  # @UndefinedVariable
        session.commit()  # @UndefinedVariable
        return item

    
class TitleDetailPipeline(object):
    
    def process_item(self, item, spider):
        user_url = processUserURL(item['user_url'])
        if 'home/main?un' in user_url and user_url not in user_bloomFilter:
            user_bloomFilter.add(user_url)
            r.lpush('tieba:user_urls', user_url)
        content=item['content'].strip()
        imgs = []
        if item['img_urls'] and len(item['img_urls']):
            for img_url in item['img_urls']:
                if img_url not in img_bloomFilter:
                    img_bloomFilter.add(img_url)
                    img = Img(title_url=item['title_url'], user_url=user_url, img_url=img_url, local_url='')
                    imgs.append(img)
                else:
                    print('img_url:%s has founded' % img_url)
        if len(content) > 0:
            detail = TitleDetail(title_url=item['title_url'], user_url=user_url,content =content )
            session.add(detail)  # @UndefinedVariable
        if len(imgs) > 0:
            session.add_all(imgs)  # @UndefinedVariable
        session.commit()  # @UndefinedVariable

    
class UserPipeline(object):
    
    def process_item(self, item, spider):
        # u = User(url=item['url'], nickName=item['nickName'], sex=item['sex'], age=item['age'], title_count=item['title_count'])
        if item:
            user_url = processUserURL(item['url'])
            u = User(url=user_url, nickName=item['nickName'], sex=item['sex'], head=item['head'])
            session.add(u)  # @UndefinedVariable
            session.commit()  # @UndefinedVariable
            return item

