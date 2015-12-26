# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class TutorialItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class DmozItem(scrapy.Item):
    Mashup_Name = scrapy.Field()
    Description = scrapy.Field()
    Category = scrapy.Field()


class AirbnbItem (scrapy.Item):
    """www.airbnb.com网站的抓取内容"""
    price = scrapy.Field()
    room_name = scrapy.Field()
    address = scrapy.Field()
    description = scrapy.Field()
    reviews_count = scrapy.Field()
    accuracy_score = scrapy.Field()
    location_score = scrapy.Field()
    communication_score = scrapy.Field()
    check_in_score = scrapy.Field()
    cleanliness_score = scrapy.Field()
    cost_performance_score = scrapy.Field()
    host_id = scrapy.Field()
    # comment_info = scrapy.Field()
    room_id = scrapy.Field()


class info (scrapy.Item):
    """房屋主人的信息"""
    host_id = scrapy.Field()
    room_name = scrapy.Field()
    room_id = scrapy.Field()


class reviews(scrapy.Item):
    """docstring for ClassName"""

    room_id = scrapy.Field()
    review = scrapy.Field()


class programmable(scrapy.Item):
    """docstring for ClassName"""
    API_Name = scrapy.Field()
    API_ID = scrapy.Field()
    Description = scrapy.Field()
    Primary_Category = scrapy.Field()
    Secondary_Categories = scrapy.Field()
    Followers_Number = scrapy.Field()
    Followers_Id = scrapy.Field()


class followers(scrapy.Item):
    API_ID = scrapy.Field()
    Followers_Name = scrapy.Field()


class mushup(scrapy.Item):
    API_ID = scrapy.Field()
    mushup_name = scrapy.Field()
