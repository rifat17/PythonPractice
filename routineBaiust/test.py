# import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.routine.baiust.edu.bd/?department_id=1&semester=12"

res = urlopen(url)

# print(res.read())

soup = BeautifulSoup(res.read(), 'html.parser')
routin = []
for tr in soup.find_all('tr'):
    dayRoutin = []
    for td in tr.find_all('td'):
        # print(td.text.strip())
        dayRoutin.append(td.text.rstrip('\n\t').strip('\n\t'))
    routin.append(dayRoutin)
    dayRoutin.clear

# print(routin)
# 

# soup = BeautifulSoup(res.read(), 'html.parser')
# # routin = []
# for tr in soup.find_all('tr'):
#     # dayRoutin = []
#     # for td in tr.find_all('td'):
#     #     # print(td.text.strip())
#     #     dayRoutin.append(td.text.strip())
#     # routin.append(dayRoutin)
#     # dayRoutin.clear
#     # print(re.sub(r'(^[ \t]+|[ \t]+(?=:))','', tr.text ))
#     # print(tr.text.rstrip('\n\t').strip('\n\t'))

# # print(routin)

for x in routin:
    # print()
    for xx in x:
        # print()
        print(xx.strip())
        # print()
    # print()