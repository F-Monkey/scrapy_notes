# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from spider.items import TiebaItem, TiebaUserItem, TitleItem
from scrapy.crawler import CrawlerProcess
from scrapy_redis.spiders import RedisSpider
import re

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36" 
headers['Accept-Encoding'] = 'gzip, deflate, br'
headers['Accept-Language'] = 'zh-CN,zh;q=0.9'
headers['Connection'] = 'keep-alive'
headers['Host'] = 'tieba.baidu.com'

baidu_base_url = 'https://tieba.baidu.com'
baidu_base_url_no_https = 'http://tieba.baidu.com'

from pybloom_live.pybloom import BloomFilter

title_url_bloom = BloomFilter(capacity=2 << 15, error_rate=0.01)


class BaiduTiebaSpider(scrapy.Spider):
    name = "tieba";
    allowed_domains = ['tieba.baidu.com']
    root_url = 'https://tieba.baidu.com/f?kw=%E7%9B%B8%E4%BA%B2&ie=utf-8&pn='

    custom_settings = {
            'ITEM_PIPELINES':{'spider.pipelines.TiebaPipeline':300},
        }
    
    MAX_DEEP_INDEX = 1000
    
    def start_requests(self):
        for i in range(self.MAX_DEEP_INDEX):
            yield scrapy.Request(url=self.root_url + str(i * 50), method='get', callback=self.parse)
        
    def parse(self, response):
        title_lis = response.xpath('//*[@id="thread_list"]/li')
        for li in title_lis:
            tiebaItem = TiebaItem()
            tiebaItem['url'] = baidu_base_url + li.xpath('.//div/div[2]/div/div/a/@href').extract_first()
            # 抓过的帖子就没必要再抓了
            if tiebaItem['url'] in title_url_bloom:
                continue 
            else:
                title_url_bloom.add(tiebaItem['url'])
            tiebaItem['title'] = li.xpath('.//div/div[2]/div/div/a/text()').extract_first()
            user_url = li.xpath('.//div/div[2]/div/div[2]/span[1]/span[1]/a/@href').extract_first()
            if 'tbmall/tshow' in user_url:  # vip sign
                user_url = li.xpath('.//div/div[2]/div/div[2]/span[1]/span[2]/a/@href').extract_first()
            tiebaItem['user_url'] = baidu_base_url_no_https + user_url
            yield tiebaItem

        
class UserSpider(RedisSpider):
    name = "user"
    
    allowed_domains = ['tieba.baidu.com']
    baidu_user_url_prffix = 'http://tieba.baidu.com'
    
    redis_key = 'tieba:user_urls'
    
    custom_settings = {
            'ITEM_PIPELINES':{'spider.pipelines.UserPipeline':300},
        }
    '''
    def start_requests(self):
        start_urls = ['http://tieba.baidu.com/home/main/?un=%E5%B0%B9%E7%B4%A0%E5%85%AE&ie=utf-%208&id=5a6fe5b0b9e7b4a0e585ae13f2&fr=frs&red_tag=l0008683305']
        for url in start_urls:
            yield scrapy.Request(url=url, method='get', callback=self.parse)
    '''

    # test
    # scrapy shell https://tieba.baidu.com/home/main/?un=%E7%8E%A9%E9%85%B7%E8%BD%A6%E5%AD%90&ie=utf-8&id=d97ee78ea9e985b7e8bda6e5ad907843&fr=frs
    def parse(self, response):
        url = response.url
        if 'home/main?un' not in url:
            return
        user = TiebaUserItem()
        user['url'] = url
        # //*[@id="userinfo_wrap"]
        # //*[@id="j_userhead"]/a/img
        user['head'] = response.xpath('//*[@id="j_userhead"]/a/img/@src').extract_first()
        user['nickName'] = response.xpath('//*[@id="userinfo_wrap"]/div[2]/div[2]/span/text()').extract_first()
        sex_class = response.xpath('//*[@id="userinfo_wrap"]/div[2]/div[3]/div/span[1]/@class').extract_first()
        user['sex'] = 'F' if 'female' in sex_class else 'M'
        # ignore ...age and title_count
        '''
        user['age'] = response.xpath('//*[@id="userinfo_wrap"]/div[2]/div[3]/div/span[2]/text()').extract_first()
        user['title_count'] = response.xpath('//*[@id="userinfo_wrap"]/div[2]/div[3]/div/span[2]/span[4]/text()').extract_first()
        '''
        yield user


class TitleDetailSpider(RedisSpider):
    name = "title"
    
    allowed_domains = ['tieba.baidu.com']
    redis_key = 'tieba:title_urls'
    
#     start_urls = ['https://tieba.baidu.com/p/6151655939']
    custom_settings = {
            'ITEM_PIPELINES':{'spider.pipelines.TitleDetailPipeline':300},
        }
    # preprocessing redis urls
    # https://github.com/rmax/scrapy-redis/blob/master/src/scrapy_redis/spiders.py
    '''
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse)
    '''       

    def parse(self, response):
        # each floor info .... include user and content   
        # //*[@id="j_p_postlist"]/div
        floors = response.xpath('//*[@id="j_p_postlist"]/div')
        for floor in floors:
            title_url = response.url
            user_url = baidu_base_url_no_https + floor.xpath('.//div[1]/ul/li[3]/a/@href').extract_first()
            content = floor.xpath('.//div[2]/div[1]/cc/div[2]').extract_first()
            # 对content进行处理：（删除表情，保留文字）
            content = re.sub(r'<.*?>', '', content).replace('\n', '').strip()
            imgs = floor.xpath('.//img[@class="BDE_Image"]/@src').extract()
            item = TitleItem()
            item['title_url'] = title_url
            item['user_url'] = user_url
            item['content'] = content
            item['img_urls'] = imgs
            yield item
        # next page 
        # //*[@id="thread_theme_5"]/div[1]/ul/li[1]/a[4]
        next_page = response.xpath('//*[@id="thread_theme_5"]/div[1]/ul/li[1]/a[contains(text(),"下一页")]/@href').extract_first()
        if next_page:
            yield scrapy.Request(url=baidu_base_url + next_page, method='get', callback=self.parse)

            
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(BaiduTiebaSpider)
    process.crawl(UserSpider)
    process.crawl(TitleDetailSpider)
    process.start()
