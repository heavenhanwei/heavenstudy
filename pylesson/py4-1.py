import urllib
import json
import ssl
from BeautifulSoup import *

url_text = raw_input('Enter URL: ')
posi = int(raw_input('Enter posi:'))
count = int(raw_input('Enter count:'))

print url_text
for i in range(0,count):
    scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    html = urllib.urlopen(url_text,context=scontext).read()
    soup = BeautifulSoup(html)
    sums = 1
    for tag in soup('a'):   
        if (sums == posi):
            print tag.get('href', url_text)
            url_text = tag.get('href', url_text)
        sums = sums + 1

