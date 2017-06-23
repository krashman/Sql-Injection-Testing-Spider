import sys
import os
#import progressbar
from time import sleep
sys.path.append("./urlS")
sys.path.append("./urlS/urlS")
sys.path.append("./urlS/urlS/spiders")

from spiders import *
from urlS_spider import MySpider
import subprocess
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log, signals
from scrapy.xlib.pydispatch import dispatcher

def stop_reactor():
    reactor.stop()

__pathToRawData = "./input/xau"
__pathToFilteredData = "./input/filtered/domainUrls.txt"
__pathToRawBannedData = "./input/rawBanned.txt"
__pathToFilteredBannedData = "./input/filtered/bannedDomainUrls.txt"
__pathToDelGarbageLists = "./scripts/delGarbageLists.py"
__pathToCheckSqlInjection = "./scripts/sqlErrorCheck/checkSQLinjection.py"


print "[==================Starting spider init...=======================]"
grepCutNumber = "cut -d',' -f2 {0}".format(__pathToRawData)
domainUrls = subprocess.check_output([grepCutNumber], shell = True)

for i,j in enumerate(domainUrls):
    data = open(__pathToFilteredData,'a+')
    data.write(j)

print "[===================Starting spider...===========================]"

dispatcher.connect(stop_reactor, signal=signals.spider_closed)
spider = MySpider()
settings = "./urlS/urlS/settings.py"
crawler = Crawler(Settings())
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.msg("------------>Running reactor")
reactor.run()
log.msg("------------>Running stoped")

print "[===================Filtering scraped data...====================]"

os.system(__pathToDelGarbageLists)

print "[===================Checking for sql injection===================]"

os.system(__pathToCheckSqlInjection)
print "DONE"


