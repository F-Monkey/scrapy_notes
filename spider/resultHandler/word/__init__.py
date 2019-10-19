from spider.io.DB import session
from spider.io.pojo import User, TitleDetail
from jieba import analyse
from _functools import reduce
from wordcloud import wordcloud
from matplotlib import colors

def anlysisUser(url):
    pass

def queryUsers(*args):
    return session.query(User)  # @UndefinedVariable

'''
    用户评论内容构建
'''
class ContentProcessor(object):
    n_s = []
    ns_s = []
    vn_s =[]
    colorMap = {}
    def __init__(self,user_url):
        self.user_url = user_url
    
    '''
        构建tags权重
    '''
    def analisysUserContent(self):
        contents = session.query(TitleDetail).filter(TitleDetail.user_url==self.user_url).all()  # @UndefinedVariable
        if len(contents) == 0:
            return []
        contents = map(lambda c : c.content ,contents)
        sentence = reduce(lambda c1,c2:c1 + c2,contents)
        tags = analyse.extract_tags(sentence=sentence ,topK=200,allowPOS=('n','ns','vn'),withWeight=True,withFlag=True)
        return tags
    '''
        根据词性构建颜色，用于区分数据信息
    '''
    def __color_fun__(self, word, font_size, position, orientation,
        font_path, random_state):
        if word in self.n_s:
            return 'green'
        elif word in self.ns_s:
            return 'red'
        elif word in self.vn_s:
            return 'blue'
    
    def buildTags2WordCloud(self,tags):
        text = {}
        for (word,flag),weight in tags:
            if 'n' == flag:
                self.n_s.append(word)
            elif 'ns' == flag:
                self.ns_s.append(word)
            elif 'vn' == flag:
                self.vn_s.append(word)
            text[word] = weight
            
        w = wordcloud.WordCloud(
                font_path = '/usr/share/fonts/truetype/SIMKAI.TTF',
                width = 1000,
                height = 700,
                background_color = 'white',
                color_func = self.__color_fun__
            )
        w.generate_from_frequencies(text)
        from spider.io import settings
        cloud_img = settings.FILE_ROOT_PATH + str(hash(self.user_url)) +'.png'
        w.to_file(cloud_img)
        return cloud_img