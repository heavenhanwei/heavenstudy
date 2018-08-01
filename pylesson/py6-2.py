import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = raw_input('Enter location: ')
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
js = json.loads(str(data))
print 'place_id:',js["results"][0]["place_id"]
    
