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
    
if __name__ == '__main__':
    s = '<div id="post_content_125867559954" class="d_post_content j_d_post_content " style="display:;">            <img class="BDE_Smiley" pic_type="1" width="30" height="30" src="https://tb2.bdstatic.com/tb/editor/images/face/i_f25.png?t=20140803">活动规则。<br>在楼下评论。<br>“六一儿童节快乐”@自己想要一起陪伴的人。<br><img class="BDE_Smiley" pic_type="1" width="30" height="30" src="https://tb2.bdstatic.com/tb/editor/images/face/i_f28.png?t=20140803">楼层点赞数前三对将获取奖品，届时可私信我，告诉我想要的童年奖品，<br>（奖品价格100元以内。小本经营）</div>'
    processContent(s)