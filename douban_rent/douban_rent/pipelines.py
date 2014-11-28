# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import json
import codecs
from scrapy.contrib.exporter import JsonLinesItemExporter

class DoubanRentPipeline(object):
    def __init__(self):
        self.file = codecs.open('douban_data_utf8.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        exporter = JsonLinesItemExporter(self.file, encoding='utf-8')
        exporter.export_item(item)
        return item

    def spider_closed(self, spider):
        self.file.close()
