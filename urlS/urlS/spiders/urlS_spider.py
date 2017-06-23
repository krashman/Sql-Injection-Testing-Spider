
#scrapy crawl urlS -o items.csv -t csv
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import *
from urlS.items import urlSitem
import writeToCsv
import re

class MySpider(CrawlSpider):
    name = "urlS"

    start_urls = []
    allowed_domains = []
    deny_domains = []

    rules = (Rule (SgmlLinkExtractor(allow_domains=(allowed_domains), deny=(deny_domains))
	, callback="parse", follow= False),
	)


    def parse(self, response):
        hxs = Selector(response)
        #Dialego xpath //a ola ta a. /@href = ola ta href attributes.To extract() emfanizi mono ta atributes
        urls = hxs.xpath('//a/@href').extract()
        items = []
        for url in urls:
          #perno mono ta link me http.....
            if re.search('^http://www.*',url):
                #filtrari osa exoun vars
                if re.search('=',url):
                    #filtrari osa einai ellinika
                    #if re.search('http://www.*.gr/.*',url):
                    item = urlSitem()
                    item ["link"] = url
                    items.append(item)
                    writeToCsv.write_to_csv(item)
        return(items)

    def __init__(self):
        #trofodoto to start urls kai to allowed domains
        for line in open('/home/kostas/AraxniProject/input/filtered/domainUrls.txt', 'r').readlines():
            #epeidi to append vazei kai ena newLine char (\n) vazo to rstrip gia na ton sviso epeidi enoxlei sto url
            self.start_urls.append('http://www.%s' % line.rstrip('\n'))
            self.allowed_domains.append('http://www.%s' % line.rstrip('\n'))
        #pernao tin lista me ta banned urls
        for bannedLine in open('/home/kostas/AraxniProject/input/filtered/bannedDomainUrls.txt'):
            self.deny_domains().append('http://www.%s' % line.rstrip('\n'))



