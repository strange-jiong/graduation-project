#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-30 10:28:03
# @Author  : jiong (447991103@qq.com)
# @Version : 0.1

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from scrapy.http import Request
from tutorial.items import AirbnbItem, info, reviews
import time
# from selenium import webdriver
import json
import re


class AirbnbSpider(scrapy.Spider):

	"""docstring for ClassName"""
	name = 'airbnb'
	allowed_domains = ['airbnb.com']
	# 测试用url
	# start_urls = [#'https://zh.airbnb.com/rooms/905492?s=LJkKsDuT',
	# 				'https://zh.airbnb.com/rooms/7327646?s=fy811GFZ'
	# 			  ]
	start_urls = [
		'https://zh.airbnb.com/s/London--United-Kingdom?source=ds',
		'https://zh.airbnb.com/s/Los-Angeles--CA?source=ds',
		'https://zh.airbnb.com/s/Tokyo--Japan?source=ds',
		'https://zh.airbnb.com/s/Boston--MA']

	def parse(self, response):
		# 这个extract() 不知道是干嘛用的，试了很久 可能是吧选择器进行转化用的。
		# 必须得从某个城市的页面中获取具体房间url送入队列，之后再爬取这个url的内容，因为在这个url页面中仍然存在大量的相同的url，所以必须进行去重的操作
		# 不要按照 chrome生成的xpath 路径 直接进行 选取 很多情况下是不行的。

		valid_urls = []
		items = []
		# 查找本页面的租房信息
		for sel in response.xpath('//div[@itemprop="description"]/span/a'):
			# print
			# len(response.xpath('//div[@itemprop="description"]/span/a'))
			url = 'https://zh.airbnb.com' + sel.xpath('@href').extract()[0]
			if url not in valid_urls:
				valid_urls.append(url)
				yield Request(url, callback=self.parse)
			else:
				pass
		# 查找下一页的租房信息,因为每个页面都记录着别的页面的信息，并不是单纯的下一页，所以必须进行url的去重
		count = response.xpath(
			'/html/body/main/div[1]/div[1]/div[6]/div[4]/div[1]/div[2]/ul/li/a')
		for sel in count:
			if len(count):
				url = 'https://zh.airbnb.com' + sel.xpath('@href').extract()[0]
				if url not in valid_urls:
					valid_urls.append(url)
					yield Request(url, callback=self.parse)
				else:
					pass

		# 将房屋主人的信息单独拿出来，送入parse3()函数中

		host = response.xpath(
			'//*[@id="host-profile"]/div/div/div/div[1]/div[1]/div/a/@href').extract()
		if host:
			url = 'https://zh.airbnb.com/s?host_id=' + \
				str(host[0].split('/')[-1])
			print url
			if url not in valid_urls:
				valid_urls.append(url)
				yield Request(url, callback=self.parse3)
			else:
				pass
		else:
			pass

		# items.extend([self.make_requests_from_url(url).replace(
		# 	callback=self.parse) for url in valid_urls])

		item = AirbnbItem()
		item['price'] = ''.join(response.xpath(
			'//div[@class="book-it__price-amount js-book-it-price-amount pull-left h3 text-special"]/text()').extract()).strip()
		temp = response.xpath(
			'//*[@id="listing_name"]/text()').extract()
		if temp:
			item['room_name'] = temp[0].strip()
		else:
			item['room_name'] = []

		temp = response.xpath(
			'//div[@id="display-address"]/a[1]/text()').extract()
		if temp:
			item['address'] = temp[0].strip()
		else:
			item['address'] = []

		# 如果评论的某个字段为空就舍弃
		# description中可能存在'\r'这样的空行，无效的空行，直接屏蔽掉
		item['description'] = []
		for sel in response.xpath('//*[@id="details"]/div/div/div/div/div[6]/div[2]/div/div[2]/div/div[1]/p/span'):
			if sel.xpath('text()').extract():
				temp = sel.xpath('text()').extract()[0].strip()
				if temp:
					item['description'].append(temp)
				else:
					pass
			else:
				pass

		item['room_id'] = response.url.split('?')[0].split('/')[-1]

		# 防止所取出的元素为空
		temp = response.xpath(
			'/html/body/main/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/a[2]/div/span/small/span[2]/text()').extract()
		if temp:
			item['reviews_count'] = temp[0].strip()
		else:
			item['reviews_count'] = []

		count = 0
		if len(item['reviews_count']):
			count = int(item['reviews_count'][0])
		room_id = item['room_id']

		# 获取评论的url

		if 0 < count < 50:
			url = 'https://zh.airbnb.com/api/v2/reviews?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=CNY&locale=zh&listing_id=%s&role=guest&_format=for_p3&_limit=%s&_offset=0&_order=language' % (
				str(room_id), str(count))
			if url not in valid_urls:
				valid_urls.append(url)
				yield Request(url, callback=self.parse4)
			else:
				pass
		else:
			a = 50
			while a <= count:
				url = 'https://zh.airbnb.com/api/v2/reviews?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=CNY&locale=zh&listing_id=%s&role=guest&_format=for_p3&_limit=%s&_offset=%s&_order=language' % (
					str(room_id), str(50), str(a - 50))
				if url not in valid_urls:
					valid_urls.append(url)
					yield Request(url, callback=self.parse4)
				else:
					pass
				a += 50
			if count % 50:
				url = 'https://zh.airbnb.com/api/v2/reviews?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=CNY&locale=zh&listing_id=%s&role=guest&_format=for_p3&_limit=%s&_offset=%s&_order=language' % (
					str(room_id), str(count % 50), str(count - count % 50))
				if url not in valid_urls:
					valid_urls.append(url)
					yield Request(url, callback=self.parse4)
				else:
					pass

		# print item['reviews_count'][0]
		# 计算星星元素有几个，判断最后一个是否为半星，计算分值
		# 星星这个实在是厉害，空白星星也是一个元素，但是却不在我所计算的list长度里，他有两批星星，其中带颜色的是覆盖在灰色星星之上的
		count = []
		count = response.xpath(
			'//*[@id="reviews"]/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div[1]/span/i')
		if len(count):
			count[-
				  1].xpath('@class').extract() == 'icon-star-half icon icon-beach icon-star-big'
			item['accuracy_score'] = len(count) - 0.5
		else:
			item['accuracy_score'] = len(count)

		count = []
		count = response.xpath(
			'//*[@id="reviews"]/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/span/i')
		if len(count):
			count[-
				  1].xpath('@class').extract() == 'icon-star-half icon icon-beach icon-star-big'
			item['location_score'] = len(count) - 0.5
		else:
			item['location_score'] = len(count)

		count = []
		count = response.xpath(
			'//*[@id="reviews"]/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/span/i')
		if len(count):
			count[-
				  1].xpath('@class').extract() == 'icon-star-half icon icon-beach icon-star-big'
			item['communication_score'] = len(count) - 0.5
		else:
			item['communication_score'] = len(count)

		count = []
		count = response.xpath(
			'//*[@id="reviews"]/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/span/i')
		if len(count):
			count[-
				  1].xpath('@class').extract() == 'icon-star-half icon icon-beach icon-star-big'
			item['check_in_score'] = len(count) - 0.5
		else:
			item['check_in_score'] = len(count)

		count = []
		count = response.xpath(
			'//*[@id="reviews"]/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[3]/div/div/div/div[1]/span/i')
		if len(count):
			count[-
				  1].xpath('@class').extract() == 'icon-star-half icon icon-beach icon-star-big'
			item['cleanliness_score'] = len(count) - 0.5
		else:
			item['cleanliness_score'] = len(count)

		count = []
		count = response.xpath(
			'//*[@id="reviews"]/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div[1]/span/i')
		if len(count):
			count[-
				  1].xpath('@class').extract() == 'icon-star-half icon icon-beach icon-star-big'
			item['cost_performance_score'] = len(count) - 0.5
		else:
			item['cost_performance_score'] = len(count)

		item['host_id'] = response.xpath(
			'//*[@id="host-profile"]/div/div/div/div[1]/div[1]/div/a/@href').extract()
		if len(item['host_id']):
			item['host_id'] = item['host_id'][0].split('/')[-1]
		else:
			pass

		# 评论这边是最大的问题，它是通过js脚本生成的，因此我们在scrapy抓取过程中就需要通过一个中间件来执行这个js代码,

		# 将得到的reponse送入浏览器引擎中
		# driver = self.browser.get(response.url)
		# 加载浏览器
		# time.sleep(5)
		# 评价的部分,进行循环
		# item['comment_info'] = []
		# for sel in response.xpath('//*[@id="reviews"]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div'):
		#     temp['content'] = sel.xpath(
		#         'div[2]/div/div[1]/div/div/p/text()').extract()
		#     temp['time'] = sel.xpath(
		#         'div[2]/div/div[2]/div[2]/div[1]/span/text()').extract()
		#     temp['id'] = sel.path(
		#         'div[1]/div[1]/a/@href') .extract()[0].split('/')[-1]
		#     item['comment_info'].append(temp)

		# 上述收集评价信息的这段代码注释掉了，并不能用，原因上面说了，因为是执行js脚本之后得到的信息，所以并不能用Xpath直接得到。

		# 后来在parse4中实现了，直接获取它进行通信得到其余评价信息的url，得到的是传递信息用的json数据，对它进行解析。

		# 将空信息滤掉,如果存在该房间记录，就将住所记录到的部分为空的信息(比如说评价之类的，部分房间是没有的)，进行改进
		if item['room_name']:
			if not item['accuracy_score']:
				item['accuracy_score'] = 0
			if not item['location_score']:
				item['location_score'] = 0
			if not item['communication_score']:
				item['communication_score'] = 0
			if not item['check_in_score']:
				item['check_in_score'] = 0
			if not item['cleanliness_score']:
				item['cleanliness_score'] = 0
			if not item['cost_performance_score']:
				item['cost_performance_score'] = 0
			yield item
		else:
			pass

	def parse2(self, response):

		valid_urls = []
		url = 'https://zh.airbnb.com/s?host_id=' + \
			response.url.split('/')[-1][0]
		if url not in valid_urls:
			valid_urls.append(url)
			yield Request(url, callback=self.parse3)
		else:
			pass

	# 爬取房间主人拥有房间的信息
	def parse3(self, response):
		# https://zh.airbnb.com/users/show/3434101
		# https://zh.airbnb.com/s?host_id=3434101

		# /rooms/905492?s=zp3AYLlk  这个加在host网页后面，即是host拥有的具体room信息

		item = info()
		item['host_id'] = response.url.split('=')[-1]
		item['room_name'] = []
		item['room_id'] = []
		for sel in response.xpath('//a[@class="text-normal"]'):
			temp1 = sel.xpath('text()').extract()[0].strip()
			# temp2 = re.findall(r'oms/(.*)?\?s',sel.xpath('@href').extract()[0])[0]
			temp2 = sel.xpath('@href').extract()[0].split(
				'rooms/')[-1].split('?s')[0].strip()
			item['room_name'].append(temp1)
			item['room_id'].append(temp2)

		yield item

	# 爬取房间的评论信息
	def parse4(self, response):

		# https://zh.airbnb.com/api/v2/reviews?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=CNY&locale=zh&listing_id=828294&role=guest&_format=for_p3&_limit=7&_offset=7&_order=language
		item = reviews()
		a = json.loads(response.body)
		# item['room_id'] = re.findall(r'listing_id=(.*)?&role', response.url)[0]
		item['room_id'] = response.url.split(
			'listing_id=')[-1].split('&role')[0]

		# 返回的是一个list，各个元素是字典，
		# comments
		# localized_date(本地端日期格式)
		# response
		# reviewee 	host_name
		#  			id
		# 			is_superhost
		# 			profile_path
		# 			profile_pic_path
		# reviewer

		item['review'] = a['reviews']  # [1]['comments']
		yield item
