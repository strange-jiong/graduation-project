#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-11 11:37:16
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import MySQLdb
import requests
from lxml import etree


conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='',
        db ='test1',
        )
cur = conn.cursor()
cur.execute("create table room_info(room_id varchar(20) ,\
									price varchar(20),\
									room_name varchar(30),\
									address varchar(10),\
									description varchar(30),\
									reviews_count varchar(30),\
									accuracy_score varchar(30),\
									location_score varchar(30),\
									communication_score varchar(30),\
									check_in_score varchar(30),\
									cleanliness_score varchar(30),\
									cost_performance_score varchar(30))")

ret = conn.fetchone()
cur.close()
conn.commit()
conn.close()
# 以上获取数据库中的id,url

#之后构建url，获取google的搜索数据
for each in  :
	url = 'http://www.google.com'
	payload = {'key1': 'value1', 'key2': 'value2'} #构建get请求
	r = requests.get(url, params=payload)

	selector = etree.HTML(html1)
	info=selector.xpath('')
	
