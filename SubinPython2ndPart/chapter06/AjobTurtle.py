#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle


# In[2]:


class AjobTurtle(turtle.Turtle):
    """AjobTurtle is a class for new type of turtle"""
    pass

if __name__ == "__main__":
    montu = AjobTurtle()
    print(type(montu))
    montu.left(30)
    montu.forward(200)
    
    turtle.done()


# In[8]:


class AjobTurtle(turtle.Turtle):
    """AjobTurtle is a class for new type of turtle"""
    
    def forward(self, pixel):
        super().backward(pixel)
    
    def backward(self, pixel):
        super().forward(pixel)
    
    def left(self, angle):
        super().right(angle)
    
    def right(self, angle):
        print("i wont turn right, because i am ajob!")
        
if __name__ == "__main__":
    montu = AjobTurtle()
    print(type(montu))
    montu.left(30)
    montu.forward(200)
    montu.left(45)
    montu.backward(100)
    montu.right(90)
    montu.forward(10)
    
    jhontu = turtle.Turtle()
    print(type(jhontu))
    jhontu.shape("turtle")
    jhontu.left(30)
    jhontu.forward(200)
    jhontu.left(45)
    jhontu.backward(100)
    jhontu.right(90)
    jhontu.forward(10)
    
    turtle.done()
        


# In[ ]:




