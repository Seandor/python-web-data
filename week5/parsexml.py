import urllib
import xml.etree.ElementTree as ET

serviceurl = raw_input('Enter location: ')

xmldata = urllib.urlopen(serviceurl).read()
tree = ET.fromstring(xmldata)
commentlist = tree.findall('comments/comment')
print 'Comments Count: ', len(commentlist)
sumresult = 0
for item in commentlist:
	count = item.find('count').text
	sumresult += int(count)
print 'The sum of numbers is: ', sumresult
