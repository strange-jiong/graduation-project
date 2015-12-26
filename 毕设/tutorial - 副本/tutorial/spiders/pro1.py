#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-11 11:07:50
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy
from scrapy.http import Request
from tutorial.items import programmable, followers, mushup
import json
import re


class proSpider(scrapy.Spider):
    """docstring for ClassName"""
    name = 'pro1'
    allowed_domains = ['programmableweb.com']
    start_urls = ['http://www.programmableweb.com/api/oxford-english-dictionary', 'http://www.programmableweb.com/api/ocr', 'http://www.programmableweb.com/api/postcode-anywhere-maps', 'http://www.programmableweb.com/api/ravegeo-webmap',
                  'http://www.programmableweb.com/api/daum-maps', 'http://www.programmableweb.com/api/fraudlabs-zipcodeworld-united-states']

    def parse(self, response):
        item = programmable()
        item['API_Name'] = response.xpath(
            """//*[@class="node-header"]/h1/text()""").extract()
        item['API_ID'] = response.xpath(
            """//li[@class="last leaf pull-left text-uppercase"]/a/@href""").extract()[0].split('/')[-1]

        item['Description'] = response.xpath(
            """//div[@class="api_description tabs-header_description"]/text()""").extract()[0].strip()
        for sel in response.xpath('//div[@class="section specs"]/div[@class="field"]'):
            if sel.xpath('label/text()').extract()[0] == 'Secondary Categories':
            	item['Secondary_Categories'] = sel.xpath('span/a/text()').extract()
            if sel.xpath('label/text()').extract()[0] == 'Primary Category':
            	item['Primary_Category'] = sel.xpath('span/a/text()').extract()
        item['Followers_Number'] = response.xpath(
			"""//section[@id="block-views-api-followers-row-top"]/div[1]/span/text()""").extract()
        yield item
