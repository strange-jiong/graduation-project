#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-16 20:03:57
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time

from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('https://zh.airbnb.com/')
time.sleep(7)
print driver.title
# data = driver.find_element_by_xpath('//*[@id="discover-recommendations"]/div[2]/div/div[3]/div/a/div/div').click()
# time.sleep(7)

# print data

# driver.find_element_by_partial_link_text('快递').click()
# time.sleep(5)
# data = driver.find_elements_by_xpath(
#     '/html/body/div[7]/div[1]/div[1]/div[2]/ul/li[1]/a')

# data=driver.find_element_by_css_selector(
#     'body > div.content.clearfix > div.main.fl > div.news.clearfix > div.news_list > ul > li:nth-child(4) > a').text

# print data
# data=driver.find_element_by_css_selector(
#     'body > div.content.clearfix > div.main.fl > div.news.clearfix > div.news_list > ul > li:nth-child(3) > a').text
# print 'jiong'
# print data

# time.sleep(10)
# driver.find_element_by_css_selector(
#     'body > div.main.clearfix > div.clearfix.act-mianbg > div.left-side > div.guests-intro > div.guests > div > div > span:nth-child(3)').text
# print data
driver.quit()
