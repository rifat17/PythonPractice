from urllib.request import urlopen 
from bs4 import BeautifulSoup as Soup 
import re
import datetime

my_url = "http://localhost:8080/routine_21-09-2019_1-03-33.html"

uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

page_soup = Soup(page_html,'html.parser')

university = page_soup.h2.text
# print(university)
dept = page_soup.h4.text
print(dept)



table = page_soup.table

tbody = table.tbody

trClass = {'Sunday' : 'bg-danger text-light',
         'Monday' : 'bg-info text-light', 
         'Thuesday' : 'bg-success text-light', 
         'Wednesday' : 'bg-dark text-light', 
         'Thusday': 'bg-primary text-light'}


# print(datetime.date.strftime(datetime.datetime.today(),'%A'))
Today = datetime.date.strftime(datetime.datetime.today(),'%A')

routine = page_soup.findAll("tr",{"class" : trClass[Today]})
# print(routine)

for sub in routine:
    Day = sub.td.b.text
    subCon = sub.findAll("div",{"class":""})

    # #print(subCon)
    print(Day)
    for x in subCon:
        # print(type(x))
        # print(len(x))
        # print(x)
        course  = x.p.text.strip()
        teacher = x.span.text
        room    = x.span.next_sibling.next_sibling.text
        # section = x.span.next_sibling.next_sibling.find_next_siblings()
        print(course,teacher,room)


    # courseID = subCon[0].text.strip()
    # teacher,room = subCon[1].text.split(',')
    # print(Day,'\n',courseID,'\n',teacher,room)


