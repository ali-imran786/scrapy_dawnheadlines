# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class DawnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # Primary Fields
    main_headline = Field()
    headline = Field()

    # Calculated Fields
    # location = Field()

    # Housekeeping Fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
