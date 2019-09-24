# import requests
# import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.routine.baiust.edu.bd/?department_id=1&semester=12"

res = urlopen(url)

# print(res.read())

soup = BeautifulSoup(res.read(), 'html.parser')

for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        print(td.text.strip())