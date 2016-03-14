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
DOWNLOAD_DELAY = 4
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
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110, #此API已经弃用
    # 'scrapy.downloadermiddlewares.useragent':None,
    # 'scrapy.downloadermiddlewares.httpproxy':None,
    # 'tutorial.mymiddlewares.ProxyMiddleware': 750, #代理需要用到
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

# 将抓取的item进行操作
ITEM_PIPELINES = {
   # 'tutorial.pipelines.MySQLStoreCnblogsPipeline': 300,
   # 'tutorial.pipelines.TutorialPipeline':300,
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
PROXIES=[
{'ip_port':'110.73.51.124:8123','user_pass':''},
{'ip_port':'110.72.47.111:8123','user_pass':''},
{'ip_port':'219.143.142.9:80','user_pass':''},
{'ip_port':'171.15.83.125:8888','user_pass':''},
{'ip_port':'106.89.163.46:80','user_pass':''},
{'ip_port':'182.90.23.233:80','user_pass':''},
{'ip_port':'182.90.15.9:80','user_pass':''},
{'ip_port':'182.88.231.59:8123','user_pass':''},
{'ip_port':'121.199.7.65:8081','user_pass':''},
{'ip_port':'121.31.198.183:8123','user_pass':''},
{'ip_port':'182.88.129.166:8123','user_pass':''},
{'ip_port':'171.212.67.187:8123','user_pass':''},
{'ip_port':'182.90.19.65:80','user_pass':''},
{'ip_port':'182.90.38.51:80','user_pass':''},
{'ip_port':'182.90.3.84:80','user_pass':''},
{'ip_port':'171.39.233.192:80','user_pass':''},
{'ip_port':'114.55.29.219:80','user_pass':''},
{'ip_port':'121.12.158.42:22','user_pass':''},
{'ip_port':'182.90.36.219:80','user_pass':''},
{'ip_port':'110.73.2.118:8123','user_pass':''},
{'ip_port':'171.36.254.94:8123','user_pass':''},
{'ip_port':'182.36.147.23:808','user_pass':''},
{'ip_port':'121.31.148.124:8123','user_pass':''},
{'ip_port':'182.90.4.247:80','user_pass':''},
{'ip_port':'110.72.45.255:8123','user_pass':''},
{'ip_port':'182.90.81.25:80','user_pass':''},
{'ip_port':'182.90.39.198:80','user_pass':''},
{'ip_port':'119.188.94.145:80','user_pass':''},
]



# end of MySQL database configure setting
