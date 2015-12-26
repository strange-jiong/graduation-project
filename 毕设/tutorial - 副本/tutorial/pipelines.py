# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import json
import codecs
# from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import MySQLdb
import MySQLdb.cursors

# 异步的那个框架用不了，不知道为什么，==搞了一整天


class TutorialPipeline(object):

	def __init__(self):
		self.conn = MySQLdb.connect(
			host='localhost',
			port=3306,
			user='root',
			passwd='',
			db='test1',
		)
		self.conn.set_character_set('utf8')
		self.cur = self.conn.cursor()

	def process_item(self, item, spider):
		# 2,3,12
		# 这里存在一个序列化保存的问题，因为mysql支持的保存类型并没有，所以需要进行序列化来保存数据结构的类型
		# 判断item的长度  存入不同的表中
		if len(item) == 2:
			self.cur.execute("insert into room_review (room_id,review) values(%s,%s)", (item['room_id'],json.dumps(item['review'])))
			print item
		elif len(item)==3:

			self.cur.execute("insert into host_room (host_id,room_id,room_name) values(%s,%s,%s)",
				(item['host_id'],
				json.dumps(item['room_id']),
				json.dumps(item['room_name'])))
			print item
		else:
			self.cur.execute("insert into room_info (room_id,host_id,price,room_name,address,description,reviews_count,accuracy_score ,location_score ,communication_score,check_in_score,cleanliness_score ,cost_performance_score) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
				(item['room_id'],
					item['host_id'],
					item['price'],
					item['room_name'],
					item['address'],
					json.dumps(item['description']),
					item['reviews_count'],
					item['accuracy_score'],
					item['location_score'],
					item['communication_score'],
					item['check_in_score'],
					item['cleanliness_score'],
					item['cost_performance_score']))
			print item
		# self.cur.close()
		self.conn.commit()
		# self.conn.close()
		# return item


# class JsonWithEncodingCnblogsPipeline(object):

#     def __init__(self):
#         self.file = codecs.open('cnblogs.json', 'w', encoding='utf-8')

#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.file.write(line)
#         return item

#     def spider_closed(self, spider):
#         self.file.close()
class SQLStorePipeline(object):

	def __init__(self):
		self.dbpool = adbapi.ConnectionPool('MySQLdb',
											db='test',
											host='localhost',
											user='root',
											passwd='',
											port=3306,
											cursorclass=MySQLdb.cursors.DictCursor,
											charset='utf8',
											use_unicode=True)

	def process_item(self, item, spider):
		# run db query in thread pool
		query = self.dbpool.runInteraction(self._conditional_insert, item)
		print 'jiong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
		query.addErrback(self.handle_error)
		return item

	def _conditional_insert(self, tx, item):
		# create record if doesn't exist.
		# all this block run on it's own thread
		tx.execute("select * from room_review where link = %s",
				   (item['room_id'], ))
		result = tx.fetchone()
		print 'jiong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
		if result:
			log.msg("Item already stored in db: %s" % item, level=log.DEBUG)
		else:
			tx.execute(
				"insert into room_review (room_id, review)\
				values (%s, %s)",
				(item['room_id'],
				 item['review'])
			)
			log.msg("Item stored in db: %s" % item, level=log.DEBUG)

	def handle_error(self, e):
		log.err(e)


class MySQLStoreCnblogsPipeline(object):

	def __init__(self, dbpool):
		self.dbpool = dbpool

		# 创建数据表
		# self.conn = MySQLdb.connect(
		# 	host='localhost',
		# 	port=3306,
		# 	user='root',
		# 	passwd='',
		# 	db='test',)
		# self.cur = conn.cursor()
		# self.cur.execute("create table room_info(room_id varchar(20) ,\
		# 									price varchar(20),\
		# 									room_name varchar(30),\
		# 									address varchar(10),\
		# 									description varchar(30),\
		# 									reviews_count varchar(30),\
		# 									accuracy_score varchar(30),\
		# 									location_score varchar(30),\
		# 									communication_score varchar(30),\
		# 									check_in_score varchar(30),\
		# 									cleanliness_score varchar(30),\
		# 									cost_performance_score varchar(30))")
		# self.cur.execute("create table host_room(host_id varchar(20) ,\
		# 										room_name varchar(1000),\
		# 										room_id varchar(300))")
		# self.cur.execute("create table room_review(room_id varchar(20) ,\
		# 											review varchar(200))")
		# self.cur.close()
		# self.conn.commit()
		# self.conn.close()

	# @classmethod
	# def from_settings(cls, settings):
	# 	dbargs = dict(
	# 		host=settings['MYSQL_HOST'],
	# 		port=setting['MYSQL_PORT'],
	# 		db=settings['MYSQL_DBNAME'],
	# 		user=settings['MYSQL_USER'],
	# 		passwd=settings['MYSQL_PASSWD'],
	# 		charset='utf8',
	# 		cursorclass=MySQLdb.cursors.DictCursor,
	# 		use_unicode=True,
	# 	)
	# 	dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
	# 	return cls(dbpool)

	# pipeline默认调用
	def process_item(self, item, spider):
		d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
		d.addErrback(self._handle_error, item, spider)
		d.addBoth(lambda _: item)
		return d

	# 将每行更新或写入数据库中
	def _do_upinsert(self, conn, item, spider):

		if len(item) == 2:
			linkmd5id = self._get_linkmd5id(item)
			# print linkmd5id
			now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
			conn.execute("""
					select 1 from room_review where linkmd5id = %s
			""", (linkmd5id, ))

			# conn.execute("""insert into room_review(room_id,review) values(%s,%s)""", (item[
			#              'room_id'], item['review']))
			ret = conn.fetchone()
			if ret:
				conn.execute("""
					update room_review set room_id = %s, review = %s where linkmd5id = %s
				""", (item['room_id'], item['review'], linkmd5id))
			# print """
			# update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
			# """, (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id)
			else:
				conn.execute("""
					insert into room_review(linkmd5id, room_id, review)
					values(%s, %s, %s)
				""", (linkmd5id, item['room_id'], item['review']))
			# print """
			#    insert into cnblogsinfo(linkmd5id, title, description, link, listUrl, updated)
			#    values(%s, %s, %s, %s, %s, %s)
			#""", (linkmd5id, item['title'], item['desc'], item['link'], item['listUrl'], now)
		else:
			pass

	# 获取url的md5编码
	def _get_linkmd5id(self, item):
		# url进行md5处理，为避免重复采集设计
		return md5(item['room_id']).hexdigest()
	# 异常处理

	def _handle_error(self, failue, item, spider):
		log.err(failure)
