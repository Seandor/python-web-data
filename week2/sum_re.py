import re

text_file = open('regex_sum_277794.txt')
numlist = list()
for line in text_file:
	line = line.rstrip()
	result = re.findall('[0-9]+', line)
	if len(result) == 0: continue
	numlist += result
print sum([int(s) for s in numlist])