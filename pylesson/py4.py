import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
#html = urllib.urlopen(url).read()

html = urllib.urlopen('http://python-data.dr-chuck.net/comments_207145.html').read()
soup = BeautifulSoup(html)
sums = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    #print 'Contents:',tag.contents[0]
    #print  'Attr:',tag.Attr
    sums = sums + int(tag.contents[0])

print sums