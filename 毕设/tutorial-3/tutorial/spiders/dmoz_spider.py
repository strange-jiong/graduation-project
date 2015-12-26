#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-23 16:34:14
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# import scrapy

# class DmozSpider(scrapy.spiders.Spider):
#     name = "dmoz"
#     allowed_domains = ["dmoz.org"]
#     start_urls = [
#         "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#         "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
#     ]

#     def parse(self, response):
#         filename = response.url.split("/")[-2]
#         with open(filename, 'wb') as f:
#             f.write(response.body)

import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "jiong"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item