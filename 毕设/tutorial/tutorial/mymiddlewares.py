#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-01 21:37:33
# @Author  : jiong (447991103@qq.com)
# @Version : 0.1

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from scrapy.exceptions import IgnoreRequest
from scrapy.contrib.downloadermiddleware import DownloaderMiddleware
import random
import base64
# from settings import PROXIES


# class RandomUserAgent(object):
#     """Randomly rotate user agents based on a list of predefined ones"""

#     def __init__(self, agents):
#         self.agents = agents

#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(crawler.settings.getlist('USER_AGENTS'))

#     def process_request(self, request, spider):
#         # print "**************************" + random.choice(self.agents)
#         # request.headers.setdefault('User-Agent', random.choice(self.agents))


# class ProxyMiddleware(object):

#     def process_request(self, request, spider):
#         proxy = random.choice(PROXIES)
#         if proxy['user_pass'] is not None:
#             request.meta['proxy'] = "http://%s" % proxy['ip_port']
#             encoded_user_pass = base64.encodestring(proxy['user_pass'])
#             request.headers[
#                 'Proxy-Authorization'] = 'Basic ' + encoded_user_pass
#             print "**************ProxyMiddleware have pass************" + proxy['ip_port']
#         else:
#             print "**************ProxyMiddleware no pass************" + proxy['ip_port']
#             request.meta['proxy'] = "http://%s" % proxy['ip_port']


"""避免被ban策略之一：使用useragent池。

使用注意：需在settings.py中进行相应的设置。
"""
# from scrapy import log
# import random
from scrapy.downloadermiddleware.useragent import UserAgentMiddleware


class RotateUserAgentMiddleware(UserAgentMiddleware):

	# user_agent_list = [
	# 	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
	# 	"(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
	# 	"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
	# 	"(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
	# 	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
	# 	"(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	# 	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
	# 	"(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
	# 	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
	# 	"(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
	# 	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
	# 	"(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
	# 	"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
	# 	"(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
	# 	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
	# 	"(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	# 	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
	# 	"(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	# 	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
	# 	"(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	# 	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
	# 	"(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
	# 	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
	# 	"(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
	# 	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
	# 	"(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	# 	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
	# 	"(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	# 	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
	# 	"(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	# 	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
	# 	"(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
	# 	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
	# 	"(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
	# 	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
	# 	"(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
	# ]
	user_agent_list = [
	    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
	    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
	    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
	    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
	    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
	    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
	    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
	    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
	    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
	    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
	    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
	]

	def __init__(self, user_agent=''):
		self.user_agent = user_agent

	def process_request(self, request, spider):
		ua = random.choice(self.user_agent_list)
		print ua
		# if ua:
		#     # 显示当前使用的useragent
		#     print "********Current UserAgent:%s************" % ua

		#     # 记录
		#     # log.msg('Current UserAgent: ' + ua, level='INFO')
		request.headers.setdefault('User-Agent', ua)

	# the default user_agent_list composes chrome,I E,firefox,Mozilla,opera,netscape
	# for more user agent strings,you can find it in
	# http://www.useragentstring.com/pages/useragentstring.php

# class CustomMiddlewares(DownloaderMiddleware):

#     def process_response(self, request, response, spider):
#         if len(response.body) == 100:
#             return IgnoreRequest("body length == 100")
#         else:
#             return response
