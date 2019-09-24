from bs4 import BeautifulSoup
import requests

url = "http://127.0.0.1:8000/Downloads/How%20to%20scrape%20websites%20with%20Python%20and%20BeautifulSoup.html"

# source = requests.get(url).text

with open('source01.html') as f:
    soup = BeautifulSoup(f, 'html5lib')


# soup = BeautifulSoup(source, features="html5lib")

# with open("source01.html","w") as f:
#     f.write(source)

print(soup.prettify())

# footer_col_2 = soup.find('site-wrapper')
# class="site-footer"
# class="footer-col-2"
# print(footer_col_2)
