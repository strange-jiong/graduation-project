# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 25

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 4
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN=16
# CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED=False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    '': 543,
# 	'tutorial.mymiddlewares.ProxyMiddleware': 544,
# }
DOWNLOADER_MIDDLEWARES = {
    #    'cnblogs.middlewares.MyCustomDownloaderMiddleware': 543,
    # 'tutorial.mymiddlewares.RandomUserAgent': 1, #随机user agent
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110, #此API已经弃用
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':1,
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110, #代理需要用到
    # 'tutorial.mymiddlewares.ProxyMiddleware': 100, #代理需要用到
    # 'scrapy_crawlera.CrawleraMiddleware': 600 , #crawlera代理用到
    # 'tutorial.mymiddlewares.RotateUserAgentMiddleware':400,
}

# DOWNLOADER_MIDDLEWARES = {
#     "tutorial.mymiddlewares.CustomMiddlewares": 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'tutorial.pipelines.MySQLStoreCnblogsPipeline': 300,
   'tutorial.pipelines.TutorialPipeline':300,
   # 'tutorial.pipelines.SQLStorePipeline':300
}
# ITEM_PIPELINES = []

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
# AUTOTHROTTLE_ENABLED=True
# The initial download delay
# AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED=True
# HTTPCACHE_EXPIRATION_SECS=0
# HTTPCACHE_DIR='httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES=[]
# HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

# 将爬虫放到scrapyhub的网上运行
# CRAWLERA_ENABLED = True
# CRAWLERA_USER = '<API key>'
# CRAWLERA_PASS = '你crawlera账号的密码'

# start MySQL database configure setting
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_DBNAME = 'test'
MYSQL_USER = 'root'
MYSQL_PASSWD = ''

# end of MySQL database configure setting
