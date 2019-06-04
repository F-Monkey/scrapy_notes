'''
Created on May 30, 2019

@author: F-Monkey

'''

def testFormate():
    root_url = 'https://tieba.baidu.com/f?kw=%E7%9B%B8%E4%BA%B2&ie=utf-8&pn='
    print(root_url+str(50))

def strTest():
    s = '吧龄:4.8年'
    print(s[3:])


def processUserURL(url):
    return url.split('&')[0]
if __name__ == '__main__':
    print(processUserURL('http://tieba.baidu.com/home/main?un=%E5%A5%A5%E4%B9%89%E5%85%AD%E9%81%93%E4%B9%8B%E8%BF%81&ie=utf-8&id=af44e5a5a5e4b989e585ade98193e4b98be8bf818b20?t=1533556137&fr=pb&red_tag=q2215799064'))