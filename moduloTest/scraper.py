from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page3.html"
dirName = 'html'
fileName = "aHtml.html"


def getCodes(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        # print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        codeList = bsObj.findAll("code",{"class":"language-bash", "class":"language-py"})
    except AttributeError as e:
        return None
    return codeList

# pyCode = getCodes(url)
#
# for code in pyCode:
#     print()
#     print(code.get_text())
#     print()

def getHtml(url=url,fileName=fileName):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    else:
        try:
            with open(dirName+'/'+fileName,'wb') as fobj:
                fobj.write(html.read())
        except FileNotFoundError as e:
            print(e)

if __name__ == "__main__":
    getHtml(url,fileName)
    # print(dirName+'/'+fileName)
