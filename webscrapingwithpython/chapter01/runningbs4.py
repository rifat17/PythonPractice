from urllib.request import urlopen
from bs4 import BeautifulSoup
'''
html    = urlopen("http://127.0.0.1:8000/Downloads/How%20to%20scrape%20websites%20with%20Python%20and%20BeautifulSoup.html")
bsObj   = BeautifulSoup(html.read(),features='html.parser')

print(bsObj.h1)
print(bsObj.html.body.h1)
print(bsObj.body.h1)
print(bsObj.html.h1)
'''
# 404 page not found                -> 1
# 500 internal server error         -> 2
# 1 & 2 both will throw HTTPError
# to handle this :

try:
    html    = urlopen("http://127.0.0.1:8000/Downloads/How%20to%20scrape%20websites%20with%20Python%20and%20BeautifulSoup.html")
except HTTPError as e:
    print(e)
else:
    # pass
    # if no error occur,
    # do whatever u want to do

    # if the server is down
    # urlopen returns a None object
    # so :

    # if html is None:
        # print("URL is not found")
    # else:
        # pass

    bsObj = BeautifulSoup(html.read(),'html.parser')
    # print(bsObj.nonExistingTag)
    # check if this html tag is exists on that page
    # if not,then it will  return None

    # the easiest solution is

    try:
        badContent  = bsObj.nonExistingTag.anotherTag
    except AttributeError as e:
        print("Tag was not found")
    else:
        if badContent == None:
            print("Tag was not found")
        else:
            print(badContent)
