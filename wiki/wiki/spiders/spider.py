# coding=utf8
import sys
from scrapy.item import Item, Field
from scrapy import Spider

from scrapy.selector import Selector
from wiki.items import WikiItem



class WikiSpider(Spider):
    name = "wiki"
    allowed_domains = ['zh.wikipedia.org']
    start_urls = ["https://zh.wikipedia.org/wiki/%E6%80%A7%E6%84%9F%E6%9F%93%E7%96%BE%E7%97%85"]

    def parse(self, response):
        print type(response)
        print response.body
#        link_list = Selector(response).xpath('a')

#        for link in link_list:
#            print link.extract()[0]
