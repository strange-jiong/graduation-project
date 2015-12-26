#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-08 21:07:03
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy
from scrapy.http import Request

from programmableweb.items import programmable, followers, mushup
# import time
# from selenium import webdriver
import json
import re


class proSpider(scrapy.Spider):

    """docstring for ClassName"""
    name = 'pro'
    allowed_domains = ['programmableweb.com']
    # 测试用url
    url = ['http://www.programmableweb.com/category-api?page=%d' %
           a for a in range(1, 8)]
    # start_urls=url.append('http://www.programmableweb.com/category-api')
    start_urls = [
        'http://www.programmableweb.com/category-api'
    ]

    def parse(self, response):
        # //*[@id='block-system-main']/div/div[1]/div/ul/li[1]/div[1]/span/a
        # //*[@id='block-system-main']/div/div[1]/div/ul/li[2]/div[1]/span/a
        # //*[@id='block-system-main']/div/div[1]/div/ul/li[60]/div[1]/span/a

        valid_urls = []

        for sel in response.xpath('//ul/li/div[1]/span/a'):
            url = 'http://www.programmableweb.com' + \
                sel.xpath('@href').extract()[0]
            if url not in valid_urls:
                valid_urls.append(url)
                yield Request(url, callback=self.parse2)
            else:
                pass
    # 本页面的下一页还没有调用自己进行解析

    def parse2(self, response):
        # //*[@id='block-system-main']/article/div[7]/div[2]/table/tbody/tr[1]/td[1]/a
        # //*[@id='block-system-main']/article/div[7]/div[2]/table/tbody/tr[100]/td[1]/a
        # //*[@id='block-system-main']/article/div[7]/div[2]/table/tbody/tr[1]/td[1]/a
        valid_urls = []
        # print "222222222!!!!!!!!!!!!!"
        for sel in response.xpath('//td[@class="views-field views-field-title col-md-3"]/a'):
            url = 'http://www.programmableweb.com' + \
                sel.xpath('@href').extract()[0]
            # print url
            if url not in valid_urls:
                valid_urls.append(url)
                yield Request(url, callback=self.parse3)
            else:
                pass
        valid_urls2 = []
        for sel in response.xpath("""//li[@class="pager-item"]/a/@href"""):
            url = 'http://www.programmableweb.com' + sel.extract()[0]
            if url not in valid_urls2:
                valid_urls2.append(url)
                yield Request(url, callback=self.parse2)
            else:
                pass

    # 本页面的下一页还没有调用自己进行解析

    def parse3(self, response):

        item = programmable()
        item['API_Name'] = response.xpath(
            """//*[@class="node-header"]/h1/text()""").extract()

        item['API_ID'] = response.xpath(
            """//li[@class="last leaf"]/a/@href""").extract()[0].split('/')[-1]

        item['Description'] = response.xpath(
            """//div[@class="api_description tabs-header_description"]/text()""").extract()[0].strip()
        item['Primary_Category'] = response.xpath(
            """//div[@class="section specs"]/div[5]/span/a/text()""").extract()
        item['Secondary_Categories'] = response.xpath(
            """//div[@class="section specs"]/div[6]/span/a/text()""").extract()
        item['Followers_Number'] = response.xpath(
            """//section[@id="block-views-api-followers-row-top"]/div[1]/span/text()""").extract()
        # http://www.programmableweb.com/api/quova/followers
        yield item
        url2 = response.url + '/followers'
        yield Request(url2, callback=self.parse4)
        # musghups
        # //*[@id='block-views-api-mashups-new-list-top']/div[2]/div[1]/a
        url3 = "http://www.programmableweb.com" + \
            response.xpath(
                "//*[@id='block-views-api-mashups-new-list-top']/div[2]/div[1]/a/@href").extract()[0]
        yield Request(url3, callback=self.parse5)

    def parse4(self, response):
        item = followers()
        # //*[@id='followers']/div[2]/div[2]/table/tbody/tr[1]/td[2]/a
        # //*[@id='followers']/div[2]/div[2]/table/tbody/tr[2]/td[2]/a
        # //*[@id='followers']/div[2]/div[2]/table/tbody/tr[17]/td[2]/a

        item['API_ID'] = response.xpath(
            '//li[@class="last leaf pull-left text-uppercase"]/a/@href').extract()[0].split('/')[-2]
        item['Followers_Name']=[]
        for sel in response.xpath("//*[@id='followers']/div[2]/div[2]/table/tbody/tr/td[2]/a"):
            temp = sel.xpath('text()').extract()[0]
            item['Followers_Name'].append(temp)
        yield item

    def parse5(self, response):
        # //*[@id='block-system-main']/article/div[7]/div[1]/table/tbody/tr[1]/td[1]/a
        # //*[@id='block-system-main']/article/div[7]/div[1]/table/tbody/tr[2]/td[1]/a
        item = mushup()
        item['API_ID'] = response.url.split('=')[-1]
        item['mushup_name']=[]
        for sel in response.xpath("//*[@id='block-system-main']/article/div[7]/div[1]/table/tbody/tr/td[1]/a"):
            temp = sel.xpath('text()').extract()[0]
            item['mushup_name'].append(temp)
        yield item
