import urllib
from BeautifulSoup import *

url = " http://python-data.dr-chuck.net/known_by_Heidi.html "
repeat_times = 7
postion = 18
name = ''

for turn in range(repeat_times):
	name_tup = get_name(url, postion)
	url = name_tup[0]
	name = name_tup[1]
print name

def get_name(url, position):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	atag = soup('a')[position-1]
	href = atag.get('href', None)
	return (href, atag.contents[0])