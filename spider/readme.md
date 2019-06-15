# scrapy note :

### 1、day01:

#### 大致描述一下自己理解的scrapy pipeline工作原理
	
##### 1、spider返回值：

spider会yield一般会yield两类数据  
	1、yield item  
	2、yield scrapy.Request(url,callback)  
前者的结果，scrapy会将结果丢给pipeline去处理，后者根据callBack丢给相应的回调函数处理

##### 2、scrapy pipeline

1、scrapy pipeline的是处理所有的结果
可是如果想指定一个pipeline来处理特定的spider处理结果，有下面几种方案

###### 1、装饰器，过滤。（不匹配抛出异常....这样比较难看）
[https://www.cnblogs.com/fly-kaka/p/5216791.html](https://www.cnblogs.com/fly-kaka/p/5216791.html)

###### 2、在pipeline中做if else判断，（判断item的类型，但是每个spider都需要改动pipeline的内容）
[https://blog.csdn.net/weixin_38859557/article/details/86220472](https://blog.csdn.net/weixin_38859557/article/details/86220472)

###### 3、在spider中添加customer_settings（比较好看）
[https://blog.csdn.net/harry5508/article/details/86486777](https://blog.csdn.net/harry5508/article/details/86486777)

-----------------------

### 2、day02:

#### 学习scrapy Middleware
	
#### 介绍
[https://www.jianshu.com/p/fa7d3e42d7da](https://www.jianshu.com/p/fa7d3e42d7da)

##### 1、Downloader Middleware

##### 2、Spider Middleware

##### 通常在middleware中实现ip切换，cookies，header，User-Agent等参数

-----------------------

### 3、day03

#### 学习settings 以及scrapy中的默认排序

-----------------------

### 4、day04

#### scrapy-redis component  
@See [spiders/__init__.py UserSpider](spider/spiders/__init__.py)

#### parse titleDetail  
@See [spiders/__init__.py](spider/spiders/__init__.py)  line:85

#### // TODO


-----------------------

### 5、day05 wordcloud & jieba  
@See [../resultHandler/word/__init__.py](../resultHandler/word/__init__.py)
1、wordcloud color_func  
2、analysis.extract_tags



### end: 杂叙

##### 1、scrapy shell

##### 2、scrapy crawl

##### 3、scrapy-redis

### 暂时没什么问题了，有些评论的内容有点长，字段长度已经增加到5000了...希望能抗住