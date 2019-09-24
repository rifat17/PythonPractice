#!/usr/bin/env python
# coding: utf-8

# In[21]:


from turtle import *
#turtle.circle(25)
forward(25)
done()


# In[26]:



color('red', 'yellow')
begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


# In[31]:


position()
done()


# In[37]:


forward(25)
position()
done()


# In[45]:


backward(30)
x,y = position()
head = heading()
done()
print('x is {} and y is {} Heading at {}'.format(x,y,head))


# In[52]:


tp1 = position()
print(tp1)
delay(1000)
setpos(60,30)
tp2 = pos()
print(tp2)
setpos(20,80)
tp3 = pos()
print(tp3)
setpos(tp1)
print(pos())
done()


# In[65]:


setheading(90)
print(position())
print(heading())
home()
print(heading())
done()


# In[70]:


home()
circle(50)
print(position())
print(heading())
done()



# In[107]:


for i in range(8):
    stamp()
    fd(30)
done()


# In[118]:


for i in range(80):
    fd(50-i)
    lt(80+i)
done()


# In[ ]:


#a lot to do

