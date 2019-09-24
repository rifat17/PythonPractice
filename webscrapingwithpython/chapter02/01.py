from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000/Downloads/How%20to%20scrape%20websites%20with%20Python%20and%20BeautifulSoup.html"


def getCodes(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        # print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        codeList = bsObj.findAll(
            "code", {"class": "language-bash", "class": "language-py"})
    except AttributeError as e:
        return None
    return codeList


pyCode = getCodes(url)


for code in pyCode:
    print()
    print(code.get_text())
    print()
