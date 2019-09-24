import re

with open('source01.html') as f:
    text = f.read()

# print(text)

p1 = re.compile(r'<div class="footer-col-2">(\s+?.+\s+?)+</div>')
t1 = re.findall(p1,text)
print(t1)
