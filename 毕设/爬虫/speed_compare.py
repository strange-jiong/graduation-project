#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-17 12:22:41
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import unittest
from selenium import webdriver
import time


class TestThree(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()
        self.url = 'http://www.baidu.com'

    def test_url_fire(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        self.driver.quit()

    def test_url_chrome(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.quit()

    def test_url_phantom(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get(self.url)
        self.driver.quit()

    def tearDown(self):
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)
        # self.driver.quit

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestThree)
    unittest.TextTestRunner(verbosity=0).run(suite)
