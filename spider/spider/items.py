# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TiebaItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    user_url = scrapy.Field()
    
    
class TiebaUserItem(scrapy.Item):
    url = scrapy.Field()
    nickName = scrapy.Field()
    sex = scrapy.Field()
    head = scrapy.Field()
    age = scrapy.Field()
    title_count = scrapy.Field()
    

class TitleItem(scrapy.Item):
    title_url = scrapy.Field()
    user_url = scrapy.Field()
    content = scrapy.Field()
    img_urls = scrapy.Field()
