#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-03 10:14:21
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import json
# metadata
# reviews 是一个list，list里面有一个字典
# 		comments
# 		response
# 		reviewee   值是一个字典
# file=open('1.txt','r')
# a=file.read()
# print a
# file.close()
b={'a':"A",'b':(2,4),'c':3.0}
# a.replace(null,None)
a=json.dumps(b)
print a
a=json.loads(a)
print a['a']




