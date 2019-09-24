from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000/PythonProjectFolder/webscrapingwithpython/chapter02/page19.html"

html = urlopen(url)

bsObj = BeautifulSoup(html, 'html.parser')

# for child in bsObj.find("table",{"id" : "giftList"}).children:
    # print(child)

for child in bsObj.find("table",{"id":"giftList"}).tr:
    print(child)

# print(bsObj.findAll('td'))