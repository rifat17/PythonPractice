import requests

# python -m http.server 8000 --bind 127.0.0.1

base = "http://127.0.0.1:8000/"

url = "http://127.0.0.1:8000/Web%20Scraping%20using%20Python%20%28article%29%20-%20DataCamp.html"

res = requests.get(url)

if res.ok:
    with open('webtext01.html','w') as tf:
        tf.write(res.text)



if res.ok:
    with open('webhtml01.html','w', encoding=res.encoding) as tf:
        tf.write(res.text)
