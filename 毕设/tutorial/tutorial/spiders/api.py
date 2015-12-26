#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-25 11:58:29
# @Author  : jiong (447991103@qq.com)
# @Version : 0.1

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy

from tutorial.items import DmozItem
class DmozSpider(scrapy.Spider):
    name = "api"
    allowed_domains = ["programmableweb.com"]
    url="http://www.programmableweb.com/category/all/mashups?page=1&apis=62687"

    start_url=["http://www.programmableweb.com/category/all/mashups?page=%d&apis=62687"%a for a in range(1,83)]
    start_url.append("http://www.programmableweb.com/category/all/mashups?apis=62687")
    start_urls=start_url

    # start_urls = [
    #     "http://www.programmableweb.com/category/all/mashups?apis=62687",
    #     "http://www.programmableweb.com/category/all/mashups?page=1&apis=62687"    # ]

    def parse(self, response):
        for sel in response.xpath('//*[@id="block-system-main"]/article/div[7]/div[1]/table/tbody/tr'):
            item = DmozItem()
            item['Mashup_Name'] = sel.xpath('td[1]/a/text()').extract()
            item['Description'] = sel.xpath('td[2]/text()').extract()
            item['Category'] = sel.xpath('td[3]/a/text()').extract()
            yield item



