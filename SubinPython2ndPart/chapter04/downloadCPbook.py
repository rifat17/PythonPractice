import requests
import sys

baseUrl = 'http://127.0.0.1:8000/'

info_dt = {"name": "Hasib", "email": "hasib@baiust.edu.bd", "country": "bangladesh"}

url = baseUrl + 'htmlSource.html'
res = requests.get(url, data=info_dt)

if res.ok is False:
    sys.exit("Failed to Download")

with open('cpbook.pdf', 'wb') as f:
    f.write(res.content)

print("Download Complete")
