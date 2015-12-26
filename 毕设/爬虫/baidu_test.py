#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-16 11:16:51
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('https://zh.airbnb.com/rooms/7897229?s=1R0W2BYf')
# print help(driver)
print driver.page_source
data = driver.find_element_by_id('cp').text
print data
driver.quit()

from selenium import webdriver

driver = webdriver.PhantomJS()#executable_path='phantomjs') #webdriver.Firefox() webdriver.PhantomJS()
driver.get('http://www.ip.cn/125.95.26.81')
print driver.find_element_by_id('range').get_attribute('id')#.split('IP')[0]#.split['IP'][1]
driver.quit()

