# -*- coding: utf-8 -*-

# Scrapy settings for urlS project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'urlS'
COOKIES_ENABLED = False
SPIDER_MODULES = ['urlS.spiders']
NEWSPIDER_MODULE = 'urlS.spiders'
REDIRECT_MAX_TIMES = 3
RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 10
DOWNLOAD_DELAY = 0.50
ROBOTSTXT_OBEY = True
AUTOTHROTTLE_ENABLED = True
CONCURRENT_REQUESTS = 600
DEPTH_LIMIT=1

ITEM_PIPELINES = {
    'project.pipelines_path.WriteToCsv.WriteToCsv' : 300
}
csv_file_path = './scripts/spiderOutput.csv'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Googlebot/2.1 ( http://www.googlebot.com/bot.html)'
