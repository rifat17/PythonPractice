import requests
import os
import webbrowser as wb

base = "http://127.0.0.1:8000/"

url = "http://127.0.0.1:8000/Web%20Scraping%20using%20Python%20%28article%29%20-%20DataCamp.html"

res = requests.get(url)

fileNmae = 'aHtmlFile.html'

with open(fileNmae,'w', encoding=res.encoding) as f:
    f.write(res.text)



# print(os.path.realpath('webhtml01.html'))
filePath = os.path.realpath(fileNmae)

print(filePath)

wb.open("file://" + filePath)

