import re

s = r'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

result = re.findall('\S+?@\S+', s)
print result

# why the non-greedy mode doesn't take effect?