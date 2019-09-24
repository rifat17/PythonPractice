import re

s = "Afganistan, America, Bangladesh, Canada, Denmark, England, Greenland, Iceland, Netherlands, New Zealand, Sweden, Switzerland"

li = re.findall(r'(\w+lands*)', s)

print(li)

match = re.search('Bangla', 'Bangladesh')
print(match)

print(match.group())

match = re.search('desh', 'Bangladesh')
print(match.group())

match = re.search('dets', 'Bangladesh')
# print(match.group())
print(match)  # result of match when not found a match!

print(type(match))
print(match is None)

s = "Bangladesh"
match = re.search('.', s)
print(match.group())

match = re.search('B.', s)
print(match.group())

match = re.search('B.n', s)
print(match.group())

match = re.search('B.n...', s)
print(match.group())


s = "Bangladesh is our homeland"

match = re.search('............', s)
print(match.group())

match = re.search("o\w\w", s)
print(match.group())

# match = re.search("i\w\w", s)
# print(match.group())
# print(match)
match = re.search("i\w", s)
print(match)
print(match.group())


match = re.search("B\w+h", s)
print()
