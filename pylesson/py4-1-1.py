import urllib
from BeautifulSoup import *

url = raw_input('Enter url: ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
count = raw_input('Enter count:')
posi = raw_input('Enter posi:')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print tag.get('href', None)