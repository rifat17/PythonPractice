# scraptest.py
from urllib.request import urlopen
html = urlopen("http://127.0.0.1:8000/Downloads/How%20to%20scrape%20websites%20with%20Python%20and%20BeautifulSoup.html")
print(html.read())
