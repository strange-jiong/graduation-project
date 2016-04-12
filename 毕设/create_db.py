#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-07 10:32:36
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import MySQLdb
"""
CREATE DATABASE cnblogsdb DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE TABLE `cnblogsinfo` (
  `linkmd5id` char(32) NOT NULL COMMENT 'url md5编码id',
  `title` text COMMENT '标题',
  `description` text COMMENT '描述',
  `link` text  COMMENT 'url链接',
  `listUrl` text  COMMENT '分页url链接',
  `updated` datetime DEFAULT NULL  COMMENT '最后更新时间',
  PRIMARY KEY (`linkmd5id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
"""
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='',
        db ='test1',
        )
cur = conn.cursor()
#创建数据表
# cur.execute("CREATE DATABASE test1 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
cur.execute("DROP TABLE IF EXISTS room_info")
cur.execute("DROP TABLE IF EXISTS host_room")
cur.execute("DROP TABLE IF EXISTS room_review")
cur.execute("create table room_info(room_id varchar(20) ,\
                                    host_id varchar(20),\
									price varchar(20),\
									room_name varchar(30),\
									address varchar(10),\
									description varchar(30),\
									reviews_count varchar(30),\
									accuracy_score varchar(30),\
									location_score varchar(30),\
									communication_score varchar(30),\
									check_in_score varchar(30),\
									cleanliness_score varchar(30),\
									cost_performance_score varchar(30))")
cur.execute("create table host_room(host_id varchar(20) ,\
										room_name varchar(1000),\
										room_id varchar(300))")
cur.execute("create table room_review(room_id varchar(20) ,\
											review varchar(200))")

# cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")

cur.close()
conn.commit()
conn.close()

