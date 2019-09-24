from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://127.0.0.1:8000/PythonProjectFolder/webscrapingwithpython/chapter02/page14.html")
bsObj = BeautifulSoup(html,'html.parser')

# namelist = bsObj.findAll("span", {"class" : "green"})
# namelist = bsObj.findAll("span", {"class" : "green", "class" : "red"})
namelist = bsObj.findAll("span", {"class" : "red", "class" : "green"})
# namelist = bsObj.findAll("span", {"class" : "red"})
# namelist = bsObj.findAll(class_="red")
# namelist = bsObj.findAll({"span"})

for name in namelist:
    print(name.get_text())
