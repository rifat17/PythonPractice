from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/Downloads/How%20to%20scrape%20websites%20with%20Python%20and%20BeautifulSoup.html'

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle(url)
if title is None:
    print("title could not be found")
else:
    print(title)
