#!/usr/bin/env python
# coding: utf-8

# In[9]:


#from datetime import datetime
import datetime


# In[11]:


#datetime.today()


# In[13]:


datetime.date.today()


# In[16]:


datetime.datetime.today()


# In[17]:


dir(datetime)


# In[19]:


dir(datetime.time)


# In[22]:


datetime.time.hour


# In[23]:


from datetime import datetime
d = datetime.today()


# In[25]:


print(d)


# In[27]:


import datetime


# In[28]:


dir(datetime)


# In[29]:


datetime.MINYEAR


# In[30]:


datetime.MAXYEAR


# In[32]:


dir(datetime.date)


# In[40]:


datetime.date.today()


# In[43]:


dir(datetime.datetime.tzinfo)


# In[50]:


from datetime import timedelta
year = timedelta(days=365)
another_year = timedelta(weeks=40,days=84,hours=23,minutes=50,seconds=600)
year.total_seconds()


# In[49]:


year == another_year


# In[51]:


import time
from datetime import date

today = date.today()


# In[52]:


today


# In[53]:


today == date.fromtimestamp(time.time())


# In[57]:


my_bday = date(today.year,12,17)
if my_bday < today:
    my_bday = my_bday.replace(year=today.year+1)
my_bday


# In[61]:


timeToBday = abs(my_bday - today)
timeToBday.days


# In[62]:


#ExampleWorkingWithDays

from datetime import date

d = date.fromordinal(730920) # 730920th day after 1. 1. 0001
d


# In[99]:


d = date.fromordinal(736948) # 736965th day after 1. 1. 0001
d


# In[100]:


t = d.timetuple()


# In[101]:


for i in t:
    print(i)


# In[102]:


ic = d.isocalendar()
ic # year,week number, day of week (1 = Monday)


# In[103]:


d.isoformat()


# In[104]:


d.strftime("%d-%m-%y")


# In[105]:


d.strftime("%A %d. %B %Y")


# In[106]:


d.strftime("%A %d. %B %y")


# In[107]:


d.strftime("%A %d. %b %Y")


# In[108]:


d.strftime("%A %D. %B %Y")


# In[109]:


d.strftime("%a %d. %B %Y")


# In[110]:


d.strftime("%a %d. %b %y")


# In[112]:


'The {1} is {0:%d}, the {2} is {0:%B}. {0:%I:%M%p}'.format(d,"day","month")


# In[ ]:




