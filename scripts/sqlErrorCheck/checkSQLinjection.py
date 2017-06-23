#!/usr/bin/python
#pernei input to out tis araxnis kai vazei sta links to <'>
#travaei html kai kitaei gia sql errors
import re
from urllib2 import urlopen, URLError
from urlparse import urlparse

def writeToFile(input):
    out = open(__pathToOutput,'a+')
    for i in input:
        out.write(i + "\n")
    print "Writing completed."
    out.close()

__pathToInput = '/home/kostas/AraxniProject/scripts/sqlErrorCheck/input.txt'  #prepi na vro tropo na min vazo olo to link
__pathToOutput = '/home/kostas/AraxniProject/scripts/sqlErrorCheck/outputVulnerable.txt'

sitesWithSqlErrors = []

with open(__pathToInput,"r") as file_: #to with volevei gia asfalia taxitita kai kanei close mono toy
    for site in file_:
        url = site.rstrip() + "'"   #to rstrip mpenei giati sto site exei \n sto telos kai ta gamaei ola
        try:
            response = urlopen(url)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
            elif hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
        else:
            html = response.read()
            patterns=re.compile(r'\bSQL\b|\bsql\b|\bquery error\b|\bMySQL\b')
            if re.search(patterns,html):
                print "POSSIBLE VICTIM FOUND in " + urlparse(url).netloc
                sitesWithSqlErrors.append(url)

writeToFile(sitesWithSqlErrors)