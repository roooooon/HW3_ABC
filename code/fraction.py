#!/usr/bin/env python
# coding: utf-8

# In[1]:


import import_ipynb
from Random import Rand


# In[2]:


class Fraction:
    
    def __init__(self):
        self.numerator = Rand()
        self.denominator = Rand()
        
    
    def fraction_calculation(self):
        return self.numerator / self.denominator
    
    
    def fraction_In(self, file):
        with open(f"{file}.txt", "a+") as f:
            f.write(f"Numerator: {self.numerator}, Denominator: {self.denominator}, Fraction: {self.fraction_calculation()} \n")
    
    
    def fraction_Out(self, file):
        with open(f"{file}.txt", "a") as f:
            f.write(f"{self.fraction_calculation()} \n")


# In[ ]:





# In[ ]:





# In[ ]:




