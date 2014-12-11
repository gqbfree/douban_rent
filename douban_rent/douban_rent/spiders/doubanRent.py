#!/usr/bin/python
#-*- coding:utf-8 -*-

from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import HTMLParser
import redis

from douban_rent.items import DoubanRentItem

r = redis.StrictRedis(host='localhost', port='6379', db=0)
r.set('url_count', 0)

class doubanRentSpider(CrawlSpider):
    name = "douban_rent"
    start_urls = ["http://www.douban.com/group/shanghaizufang/"]
    allowed_domains = ["douban.com"]
    rules = [
            Rule(SgmlLinkExtractor(allow=(r'http://www.douban.com/group/shanghaizufang/discussion\?start=\d+'))),
            Rule(SgmlLinkExtractor(allow=(r'http://www.douban.com/group/topic/\d+')), callback="parse_rent"),
    ]

    def parse_rent(self, response):
        sel  = Selector(response)
        item = DoubanRentItem() 
        html_parser = HTMLParser.HTMLParser()

        item['title'] = "".join(sel.xpath('//*[@id="content"]/h1/text()').extract())
        item['link']  = response.url
        item['desc']  = "".join(sel.xpath('//*[@id="link-report"]/div/p/text()').extract())

        self.state['url_count'] = self.state.get('url_count', 0) + 1
        return item
