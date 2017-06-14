# 毕业设计的爬虫实现
## 实现

所用框架为python+scrapy，前期使用的测试平台为[这个](https://dash.scrapinghub.com/)(需要注册)，之后打算在本地跑，存入MySQL数据库中，方便进行数据分析。

### 关于middlewares（中间件）的使用
### pipelines.py的定义
mysql数据库实现异步存储

## 使用
以后再说。

* 如果需要在网上平台进行测试，需要在 *scrapy.cfg* 同一目录，使用 *shub deploy* 命令


This is [scrapy中文教程](http://scrapy-chs.readthedocs.org/zh_CN/latest/intro/tutorial.html).

## 目前的问题
- 在本地跑的时候仍然会出现跑200多次就被被禁ip的情况。

- 年前（2015）爬取airbnb好像user-agent不做修改并没有问题，年后直接被封，已经将源码的downloadmiddleware中修改useragent的插件进行修改，可以顺利爬取。

- 想在后续加入代理池进行尝试
- 控制爬取速率，时间，看能不能分时进行爬取
