#!/usr/bin/python
from urlparse import urlparse
import re
import sys


def callIceCream():
    print "     __________________________"
    print "   _{                           }_"
    print "  {                               }"
    print " {                                 }"
    print " --------===================--------"
    print " =                                 ="
    print " =  |-------|           |-------|  ="
    print " =  |||||||||           |||||||||  ="
    print " =   |||||||             |||||||   ="
    print " =    |||||               |||||    ="
    print " =     |||        |        |||     ="
    print " =                |                ="
    print " =                l                ="
    print " =                 ~__             ="
    print " =                                 ="
    print " =   |\                       /|   ="
    print " =   | \=====================/ |   ="
    print " =    \  !!    !!    !!   !!  /    ="
    print " =     \ !!    !!    !!   !! /     ="
    print " =      \===================/      ="
    print " =                                 ="
    print " =                                 ="
    print " =---------------------------------="
    print "                 ||"
    print "                 ||"
    print "                 ||"
    print "                 ||"
    print "                 ||"
    print "                 ||"
    print "                 ||"
    print "                 ||"
    print "                 ||"
    print "                 ||"


def writeGoodLinks(linksList):
    goodLinksFile = open(__PathcleanDataFile,'a+')
    for i in goodLinks:
        goodLinksFile.write(i)
    print "Filtering Completed!! ===b"
    goodLinksFile.close()

callIceCream()

__PathdirtyDataFile = '/home/kostas/AraxniProject/scripts/spiderOutput.csv'
__PathcleanDataFile = '/home/kostas/AraxniProject/scripts/sqlErrorCheck/input.txt' #pass to sqlErrorCheck.py
goodLinks = []
index = 0
idx=0

print 'Starting IceFilter, long waiting time process.',
sys.stdout.flush()

for inputLink in open(__PathdirtyDataFile,'r').readlines():
    regexBanned = re.search(r'google|facebook.com|youtube.com|yahoo.com|baidu.com|wikipedia.org|live.com|twitter.com|qq.com|msn.com|yahoo.co.jp|linkedin.com|taobao.com|google.co.in|sina.com.cn|amazon.com|wordpress.com|google.com.hk|google.de|bing.com|google.co.uk|yandex.ru|ebay.com|163.com|google.co.jp|google.fr|microsoft.com|paypal.com|google.com.br|mail.ru|craigslist.org|fc2.com|google.it|apple.com|google.es|imdb.com|google.ru|weibo.com|vkontakte.ru|sohu.com|bbc.co.uk|ask.com|tumblr.com|livejasmin.com|xvideos.com|go.com|youku.com|bp.blogspot.com|cnn.com|soso.com|google.ca|aol.com|tudou.com|xhamster.com|ifeng.com|megaupload.com|mediafire.com|zedo.com|ameblo.jp|pornhub.com|google.co.id|godaddy.com|adobe.com|about.com|rakuten.co.jp|espn.go.com|alibaba.com|conduit.com|ebay.de|4shared.com|wordpress.org|livejournal.com|google.com.mx|google.com.tr|livedoor.com|yieldmanager.com|google.com.au|blogger.com|youporn.com|renren.com|cnet.com|uol.com.br|google.pl|myspace.com|ebay.co.uk|chinaz.com|nytimes.com|thepiratebay.org|doubleclick.com',inputLink)
    if regexBanned is None:
        flagStepOver = False
        for index,goodLink in enumerate(goodLinks):
            inputLinkNetloc = urlparse(inputLink).netloc
            goodLinkNetloc = urlparse(goodLink).netloc
            if inputLinkNetloc == goodLinkNetloc:
                goodlinkQuery = urlparse(goodLink).query
                inputLinkQuery = urlparse(inputLink).query
                if len(inputLinkQuery) > len(goodlinkQuery):    #replace link
                    idx = idx - 1
                    del goodLinks[idx]
                    goodLinks.append(inputLink)
                    print '[',inputLink,'] inserting/replacing...'
                    idx = idx + 1
                    flagStepOver = True #gia na min ektelesti to if sto telos
                else:
                    #print '         (len)inputLinkQuery < (len)goodlinkQuery DO NOTHING'
                    flagStepOver = True
        if flagStepOver == False:
            #print 'Link not found... inserting...\n'
            goodLinks.append(inputLink)
            idx = idx+1
    else:
        regexBanned = None
        pass

writeGoodLinks(goodLinks)
