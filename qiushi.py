# -*- coding: utf-8 -*-
#小白练手项目1-跟静觅大大学爬虫
import urllib2
import urllib
import re

###读取页面，注意
class QSBK():
    def __init__(self):
        self.page=1
        self.user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
        self.headers={'User-Agent' : self.user_agent}
        self.stories=[] #存放段子的变量，每一个元素是每一页的段子们

    def getPage(self,page): ####获取页面内容
        try:
            url = 'https://www.qiushibaike.com/text/page/' + str(page)
            request=urllib2.Request(url,headers=self.headers)
            response=urllib2.urlopen(request)
            content = response.read()#.decode('utf-8')
            return content
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print u'错误原因是：',e.code  ###u 用法
                return None

    def getPageContent(self):  ###页面正则匹配，获取内容，（）内的内容注意下
        content=self.getPage(self.page)
        if not content:    ###判断是否为none if content is not None 貌似不等价
            print u'页面加载不出，请返回'
            return None
        pattern = re.compile(
                '<div.*?class="content">.*?<span>(.*?)</span>.*?<div.*?class="stats">.*?<span.*?class="stats-vote">.*?<i.*?class="number">(.*?)</i>',
                re.S)  ####获取内容、笑脸数
        items = re.findall(pattern, content)
        for item in items:
            self.stories.append([item[0].strip().replace('<br/>',''), item[1].strip()])
            return self.stories

    def writeText(self): #写入文件
        qiushitext=open('D:\wenjian\qiushi.txt','w+') #注意字符串类型问题
        try:
            for item in self.stories:
                qiushitext.write(item[0])
                qiushitext.write(item[1])
            print u'写入成功'
        finally:
            qiushitext.close()

    def main(self):
        print u'正在爬取……'
        self.getPageContent()
        self.writeText()
        print u'爬取结束'

spider = QSBK()
spider.main()


#待解决问题：1、读入内容为何只有第一个 2、翻页问题后续添入 
