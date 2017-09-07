# -*- coding: utf-8 -*-
import scrapy
from quotesbot.items import DmozItem


class QQSpider(scrapy.Spider):
    name = "qq"
    start_urls = [
        'http://news.qq.com/',
    ]

    def parse(self, response):
      
        for sel in response.xpath('//div/em'):
            item =DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            yield item
            print item['title']                        


#print response.css('a[class=linkto]::text')[0].extract().encode('utf-8')