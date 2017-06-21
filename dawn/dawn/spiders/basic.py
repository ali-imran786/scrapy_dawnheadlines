# -*- coding: utf-8 -*-
import scrapy
from dawn.items import DawnItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['www.dawn.com']
    start_urls = ['https://www.dawn.com/']

    def parse(self, response):
        item = DawnItem()
        item['main_headline']=response.xpath('//h2[@class="story__title    size-seven  text--italic    "]//a').extract()
        item['headline']=response.xpath('//h2[@class="story__title    size-four    "]//a').extract()

        item['url']=response.url
        item['project']=self.settings.get('BOT_NAME')
        item['spider']=self.name
        # item['server']=socket.gethostname()
        # item['date']=datetime.datetime.now()
        return item
