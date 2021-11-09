#!/usr/bin/env python
# coding: utf-8

# In[1]:


import import_ipynb
from Random import Rand
import math


# In[2]:


class ComplexNumber:
    
    def __init__(self):
        self.real = Rand()
        self.imaginary = Rand()
        
    
    def c_In(self, file):
        with open(f"{file}.txt", "a+") as f:
            f.write(f"Real: {self.real} Imaginary: {self.imaginary} Complex: {self.complex_calculation()} \n")
    
    
    def complex_calculation(self):
        return math.sqrt(self.real * self.real + self.imaginary * self.imaginary)
    
    
    def c_Out(self, file):
        with open(f"{file}.txt", "r") as f:
            print(f.read())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




