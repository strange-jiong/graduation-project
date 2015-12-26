#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-23 11:21:37
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys) 
sys.setdefaultencoding('utf-8')



# from ghost import Ghost
import ghost
# ghost = Ghost()
# help(ghost)
page, extra_resources = ghost.open("http://xiaorui.cc")
assert page.http_status==200 and 'xiaorui' in ghost.content