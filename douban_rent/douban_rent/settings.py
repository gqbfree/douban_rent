# Scrapy settings for douban_rent project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'douban_rent'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['douban_rent.spiders']
NEWSPIDER_MODULE = 'douban_rent.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = {
#    'douban_rent.mongo_pipelines.MongoDBPipeline':300,
    'douban_rent.pipelines.DoubanRentPipeline':400,
}

DOWNLOAD_DELAY=2
RANDOMIZE_DOWNLOAD_DELAY=True
USER_AGENT='Mozilla/5.0(Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, link Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIE_ENABLE = True

MONGODB_SERVER = 'localhost'
MONGODB_PORT   = 27017
MONGODB_DB     = 'python'
MONGODB_COLLECTION = 'test'
