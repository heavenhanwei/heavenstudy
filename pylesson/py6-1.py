import json
import urllib

url = raw_input('Enter url: ')
data = urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'
info = json.loads(data)
print 'User count:', len(info['comments'])
sums = 0

for item in info['comments']:
	sums = sums + int(item['count'])

print 'Sums:',sums 
   # print 'Name', item['name']
   # print 'Id', item['id']
   # print 'Attribute', item['x']