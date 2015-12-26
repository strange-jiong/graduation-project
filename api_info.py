#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Date    : 2015-12-11 11:37:16
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb
import requests,urllib2,random
from lxml import etree

 
# conn= MySQLdb.connect(
#         host='localhost',
#         port = 3306,
#         user='root',
#         passwd='',
#         db ='test1',
#         )
# cur = conn.cursor()
# cur.execute("create table room_info(room_id varchar(20) ,\
# 									price varchar(20),\
# 									room_name varchar(30),\
# 									address varchar(10),\
# 									description varchar(30),\
# 									reviews_count varchar(30),\
# 									accuracy_score varchar(30),\
# 									location_score varchar(30),\
# 									communication_score varchar(30),\
# 									check_in_score varchar(30),\
# 									cleanliness_score varchar(30),\
# 									cost_performance_score varchar(30))")

# ret = conn.fetchone()
# cur.close()
# conn.commit()
# conn.close()


user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0', \
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0', \
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \
        (KHTML, like Gecko) Element Browser 5.0', \
        'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)', \
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', \
        'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14', \
        'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \
        Version/6.0 Mobile/10A5355d Safari/8536.25', \
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/28.0.1468.0 Safari/537.36', \
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']
def search(self, queryStr):
    queryStr = urllib2.quote(queryStr)
    url = 'https://www.google.com.hk/search?hl=en&q=%s' % queryStr
    request = urllib2.Request(url)
    index = random.randint(0, 9)
    user_agent = user_agents[index]
    request.add_header('User-agent', user_agent)
    response = urllib2.urlopen(request)
    html = response.read()
    results = self.extractSearchResults(html)


# example 'http://allogarage.wordpress.com/2007/11/15/api-allogarage/'
# for each in  :
# def search(self, queryStr):
queryStr='http://allogarage.wordpress.com/2007/11/15/api-allogarage/'
#queryStr='https://dev.twitter.com/rest/public'
queryStr = urllib2.quote(queryStr)
print queryStr
url = 'https://www.google.com.hk/search?q=%s&newwindow=1&safe=active&hl=en&lr=lang_en&sa=X&ved=0ahUKEwi9kcu8x-XJAhUHIqYKHW1dCfQQuAEIIA&biw=1440&bih=775' % queryStr
request = urllib2.Request(url)
index = random.randint(0, 9)
user_agent = user_agents[index]
request.add_header('User-agent', user_agent)
response = urllib2.urlopen(request)
html = response.read()
print html
selector = etree.HTML(html)
info=selector.xpath('//*[@id="rso"]/div/div[1]/div/div/div/span/text()')
# //*[@id="rso"]/div[1]/div/div/div/div/span
# //*[@id="rso"]/div/div[1]/div/div/div/span
# //*[@id="rso"]/div[1]/div/div/div/div/span
# print info[3].xpath('text()')
print info

# print html
# https://www.google.com.hk/search?q=http%3A//allogarage.wordpress.com/2007/11/15/api-allogarage/
# results = extractSearchResults(html)

# url1='http://allogarage.wordpress.com/2007/11/15/api-allogarage/'
# url = 'http://www.google.com.hk/search'
# payload = {'hl': 'en', 'q': url1}
# r = requests.get(url, params=payload)
# print r.text

# print 'jiong'
