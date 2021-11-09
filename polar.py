#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import import_ipynb
from Random import Rand


# In[2]:


class Polar:
    
    def __init__(self):
        self.angle = Rand()
        self.radius = Rand()
        
    
    def polar_calculation(self):
        return self.radius
    
    
    def polar_InRnd(self):
        self.radius = math.random()
        self.angle = math.random()
        
        
    def polar_Out(self, file):
        with open(f"{file}.txt", "r") as f:
            print(f.read())
    
    def polar_In(self, file):
        with open(f"{file}.txt", "a+") as f:
            f.write(f"Angle: {self.angle}, Radius: {self.radius} Polar: {self.polar_calculation()} \n")


# In[ ]:





# In[ ]:





# In[ ]:




