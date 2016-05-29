import json
import urllib

request_url = raw_input('Enter location: ')
print 'Retrieving ', request_url
jsondata = urllib.urlopen(request_url).read()
info = json.loads(jsondata)
print info

sumresult = 0
for comment in info['comments']:
	count = comment['count']
	sumresult += int(count)
print 'The sum of Number is: ', sumresult