#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-19 10:43:26
# @Author  : jiong (447991103@qq.com)
# @Version : 0.1

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pyspider.libs.base_handler import *

class Handler(BaseHandler):
    crawl_config = {}

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://scrapy.org/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():

            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
    	print response.url,response.doc('title').text()
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
