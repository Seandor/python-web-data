import urllib
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/comments_277799.html "
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

result = 0
for span in soup('span'):
	result += int(span.contents[0])

print result