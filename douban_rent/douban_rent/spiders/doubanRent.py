#!/usr/bin/python
#-*- coding:utf-8 -*-

from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import HTMLParser

from douban_rent.items import DoubanRentItem

class doubanRentSpider(CrawlSpider):
    name = "douban_rent"
    start_urls = ["http://www.douban.com/group/shanghaizufang/"]
    allowed_domains = ["douban.com"]
    rules = [
            Rule(SgmlLinkExtractor(allow=(r'http://www.douban.com/group/shanghaizufang/discussion\?start=\d+'))),
            #Rule(SgmlLinkExtractor(allow=(r'http://www.douban.com/group/shanghaizufang/discussion\?start=^[\w\W]{0,20}'))),
            Rule(SgmlLinkExtractor(allow=(r'http://www.douban.com/group/topic/\d+')), callback="parse_rent"),
    ]

    def __del__(self):
        with open('/home/qingbo_gao/martin/scrapy/project/douban_rent/info.txt', 'w') as f:
            f.write(self.state['url_count'])
    

    def parse_rent(self, response):
        sel  = Selector(response)
        item = DoubanRentItem() 
        html_parser = HTMLParser.HTMLParser()

        item['title'] = "".join(sel.xpath('//*[@id="content"]/h1/text()').extract())
        item['link']  = response.url
        item['desc']  = "".join(sel.xpath('//*[@id="link-report"]/div/p/text()').extract())

        self.state['url_count'] = self.state.get('url_count', 0) + 1

        return item
