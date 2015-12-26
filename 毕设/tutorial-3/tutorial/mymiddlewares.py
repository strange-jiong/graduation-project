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

	user_agent_list = [
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
		"(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
		"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
		"(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
		"(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
		"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
		"(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
		"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
		"(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
		"(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
		"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
		"(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
		"(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
		"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
		"(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
		"(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
		"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
		"(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
		"(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
		"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
		"(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
		"(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
		"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
		"(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
		"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
		"(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
		"(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
		"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
		"(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
	]

	def __init__(self, user_agent=''):
		self.user_agent = user_agent

	def process_request(self, request, spider):
		ua = random.choice(self.user_agent_list)
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
