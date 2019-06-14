'''
Created on May 30, 2019

@author: F-Monkey

'''
import re

def testFormate():
    root_url = 'https://tieba.baidu.com/f?kw=%E7%9B%B8%E4%BA%B2&ie=utf-8&pn='
    print(root_url+str(50))

def strTest():
    s = '吧龄:4.8年'
    print(s[3:])


def processUserURL(url):
    return url.split('&')[0]

def processContent(s):
    s = re.sub(r'<.*?>','',s)
    print(s.replace('\n', '').strip())

def testRange():
    for i in range(1000,0,-1):
        print(i)

if __name__ == '__main__':
    testRange()
    