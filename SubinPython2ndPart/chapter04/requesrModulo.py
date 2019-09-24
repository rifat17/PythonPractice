import requests

# python -m http.server 8000 --bind 127.0.0.1

base = "http://127.0.0.1:8000/"

url = "http://127.0.0.1:8000/Web%20Scraping%20using%20Python%20%28article%29%20-%20DataCamp.html"

response = requests.get(url)

print(response)
print(response.status_code)
# print(response.text)
# print(response.json)
# print(response.url)
# print(response.reason)
# print(type(response))
# print(response.is_redirect)
# print(response.apparent_encoding)
# print(response.close)
# print(response.connection)
# print(response.content)
# print(response.cookies)
# print(response.headers)
# print(response.history)
# print(response.next)
# print(response.ok)
# print(response.links)
# print(response.iter_content)
print(response.iter_lines)
print(dir(response))