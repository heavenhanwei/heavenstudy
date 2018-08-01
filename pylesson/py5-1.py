import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_207142.xml'
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
commentinfo = ET.fromstring(data)
filelist = commentinfo.findall('.//comment')
print 'Count:',len(filelist)
sums = 0

for item in filelist:
	sums = sums + int(item.find('count').text)

print 'sums:',sums



# http://python-data.dr-chuck.net/comments_42.xml