'''
Created on 2019-06-14

@author: F-Monkey
'''
from resultHandler.word import queryUsers, ContentProcessor
import json
from _functools import reduce
dict = {}

def testQueryUser():
    users = queryUsers()
    for u in users:
        print(str(u))
def testAnalysisWords():
    url = 'http://tieba.baidu.com/home/main?un=%E6%97%A0%E5%90%8D12345678xs'
    cp = ContentProcessor(url)
    tags = cp.analisysUserContent()
    cp.buildTags2WordCloud(tags)
    

def testReduce():
    l = ['1','2','3']
    result = reduce(lambda v1,v2:v1+v2,l)
    print(result)

if __name__ == '__main__':
    testAnalysisWords()