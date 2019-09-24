# import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

# url = "http://www.routine.baiust.edu.bd/?department_id=1&semester=12"

url = 'http://127.0.0.1:8000/routineBaiust/routine_21-09-2019_1-03-33.html'

res = urlopen(url)

# print(res.read())

soup = BeautifulSoup(res.read(), 'html.parser')
# routin = []
# for tr in soup.find_all('tr'):
#     dayRoutin = []
#     for td in tr.find_all('td'):
#         # print(td.text.strip())
#         dayRoutin.append(td.text.rstrip('\n\t').strip('\n\t'))
#     routin.append(dayRoutin)
#     dayRoutin.clear

# print(routin)
# 

# soup = BeautifulSoup(res.read(), 'html.parser')
# # routin = []
# for tr in soup.find_all('tr'):
#     # dayRoutin = []
#     # for td in tr.find_all('td'):
#     #     # print(td.text.strip())
#     #     dayRoutin.append(td.text.strip())
#     # routin.append(dayRoutin)
#     # dayRoutin.clear
#     # print(re.sub(r'(^[ \t]+|[ \t]+(?=:))','', tr.text ))
#     # print(tr.text.rstrip('\n\t').strip('\n\t'))

# # print(routin)

# for x in routin:
#     # print()
#     for xx in x:
#         # print()
#         print(xx.strip())
#         # print()
#     # print()




# print(soup)


# routin = []
# for tr in soup.find_all('tr'):
#     dayRoutin = []
#     # tr = tr.strip('\n\t')
#     for td in tr.find_all('td'):
#         # print(td.text.strip())
#         x = td.text.rstrip('\n\t').strip('\n\t')
#         x = x.replace(' ','')
#         dayRoutin.append(x)
        
#     routin.append(dayRoutin)
#     dayRoutin.clear

# # print(len(routin))
# # # print(routin[2])
# # for x in routin[2]:
# #     # x = x.strip()
# #     x = x.replace(' ','')
# #     print(x)

# print(routin[1])
