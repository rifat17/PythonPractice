from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://www.google.com/"
html = urlopen(url)

with open("aRokomariPage.html",'wb') as fObj:
    fObj.write(html.read())
