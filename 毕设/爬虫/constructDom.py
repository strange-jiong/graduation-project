#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-16 15:10:04
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import subprocess

def getDom(url):
	cmd='phantomjs ./constructDom.js "%s"'%url
	print 'cmd=',cmd
	stdout,stderr=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print stdout
	return stdout

if __name__ == '__main__':
	getDom('http://www.qq.com/')





