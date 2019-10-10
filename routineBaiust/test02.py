from urllib.request import urlopen 
from bs4 import BeautifulSoup as Soup 
import re
import datetime

# my_url = "http://localhost:8080/routine_21-09-2019_1-03-33.html"

my_url = 'http://routine.baiust.edu.bd/?department_id=1&semester=12'

uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

page_soup = Soup(page_html,'html.parser')

university = page_soup.h2.text
# print(university)
dept = page_soup.h4.text
print(dept)
# page_soup.table.findAll('th')  

# for i in page_soup.table.findAll('th'): 
#     print(i.text)

# for i in page_soup.table.findAll('th'): 
#     print(i.text);print() 


# for i in page_soup.table.findAll('th'): 
#     time = i.text.split() 
#     print(time)



# for i in page_soup.table.findAll('th'): 
#     time = i.text.split('-') 
#     print(time)

# header = page_soup.find("div", {"class":"card"})
# # header = page_soup.h4.p
# print(header.div.text)

# header = page_soup.find("div", {"class":"card-body table-responsive"})
# # header = page_soup.h4.p
# print(header.div.p.text)



# times = []  
# for i in page_soup.table.findAll('th'): 
#     time = i.text.split('-') 
#     print(time) 
#     times.append(time)




# times = []  
# for i in page_soup.table.findAll('th'): 
#     time = i.text.split() 
#     print(time) 
#     times.append(time) 

# page_soup.table.td
# page_soup.table.tr


# page_soup.table.tbody 
# page_soup.table.tbody.tr

# day = page_soup.table.tbody.tr.td.text

# page_soup.table.tbody.tr.div   

# page_soup.table.tbody.tr.div.p

# page_soup.table.tbody.tr.div.findAll('p')


# for r in page_soup.table.tbody.tr.div.findAll('p'): 
#     print(r.text) 


# for r in page_soup.table.tbody.tr.findAll('p'): 
#     print(r.text.strip())



# for r in page_soup.table.tbody.tr.findAll('td'): 
#     print(r.text.strip()) 

# tBody = page_soup.table.tbody
# # print( tBody )

# trInsideTbody = tBody.tr

# # print(trInsideTbody.text)

# # print(trInsideTbody.findAll('div'))

# subCode = ''
# teacher = []
# classRoom = ''

# for div in trInsideTbody.findAll('div'):
#     subCode = div.p.text
#     for i in div.findAll({'span':''}):
#         # teacher.append(i.text)
#         print(i.text)


# print(subCode)
# print(teacher)



# for x in page_soup.table.tbody.tr.div.findAll({'p':''}):
#     print(x.text)


# for tr in page_soup.table.tbody.findAll('tr'):
#     for x in tr.div.findAll({'p':''}):
#         print(x.text)


# for tr in page_soup.table.tbody.findAll('tr'):
# for tr in page_soup.table.tbody.tr.findAll('td'):
#     # print(tr)
#     # for td in tr.findAll('td'):
#         # print(td.text)
#         # pass
#         # print(td.children)
#         for x in tr.descendants:
#             print(x.string)

# print(page_soup.get_text())

# tbody = page_soup.table.tbody

# # print(tbody)
# td = []
# # for atd in tbody.tr.findAll('td'):
# #     td.append(atd)

# # for atd in td:
# #     # print(atd.text.strip())
# #     pass


# tr = []
# for atr in tbody.findAll('tr'):
#     tr.append(atr)
#     for atd in atr.findAll('td'):
#         td.append(atd)

# for atd in td:
    # print(atd.text.strip())

# print(type(tr))
# print(len(tr[0]))
# print((tr[1]))
# print((td[2]))


# works fine
# try:
#     for atd in td:
#         txt = atd.text
#         txt = txt.strip()
        
#         l = txt.splitlines()
#         if len(txt) > 0:
#             print(l[0])
#             pass
#         if len(atd) > 1:
#             print(l[1])
#         print()
# except Exception as e:
#     print(e)


# table = page_soup.table

# # print(table)

# # with open('table.html','a') as f:
# #     f.write(str(table))
# aax = []
# textt = []
# # for ax in table.findAll('tr',{"class" : "bg-danger text-light"}):
# for ax in table.findAll(class_=re.compile(r'bg-\w+ text-light')):
#     # print(ax.text.strip())
#     # print(type(ax))
#     aax.append(ax)
#     textt.append(ax.text.strip())
# # print((textt[0]).replace('\n',' ').replace('\t',' ').strip())
# # print(type(textt[0]))
# sunday = textt[0]

# sunday = (sunday.replace('\n','|'))

# # print(type(sunday))
# sunday = (sunday.replace('  ',''))
# # print(sunday.split('|'))

# print(aax[0].prettify())

# for a in aax:
#     # print(a.prettify())
#     for tdd in a.findAll('td'):
#         # print(tdd.b.text)
#         print(tdd.div.text)

table = page_soup.table

tbody = table.tbody

trClass = {'Sunday' : 'bg-danger text-light',
         'Monday' : 'bg-info text-light', 
         'Thuesday' : 'bg-success text-light', 
         'Wednesday' : 'bg-dark text-light', 
         'Thursday': 'bg-primary text-light'}


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


