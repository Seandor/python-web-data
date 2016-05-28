import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/search1.py')

for line in fhand:
	print line