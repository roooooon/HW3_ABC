#!/usr/bin/env python
# coding: utf-8

# In[1]:


import import_ipynb
from Random import Rand
from polar import Polar
from fraction import Fraction
from complex_numbers import ComplexNumber
import random


# In[2]:


class Number:
    
    def __init__(self):
        self.k = random.choice(["POLAR", "COMPLEX", "FRACTION"])
    
    
    def num_InRnd(self):
        if self.k == "COMPLEX":
            self.c = ComplexNumber()
        elif self.k == "POLAR":
            self.p = Polar()
        elif self.k == "FRACTION":
            self.f = Fraction()
        else:
            return False
        return self.num_calculation()
    
    
    def num_calculation(self):
        if self.k == "COMPLEX":
            return self.c.complex_calculation()
        elif self.k == "FRACTION":
            return self.f.fraction_calculation()
        elif self.k == "POLAR":
            return self.p.polar_calculation()
        else:
            return 0.0
        
    
    def num_In(self, file):
        if self.k == "COMPLEX":
            self.c.c_In(file)
            return True
        elif self.k == "FRACTION":
            self.f.fraction_In(file)
            return True
        elif self.k == "POLAR":
            self.p.polar_In(file)
            return True
        else:
            return False
        
#     def num_Out(self):
#         if COMPLEX:
#             c_Out(n.c, ofst)
#             break
#         elif FRACTION:
#             fraction_Out(n.f, ofst)
#             break
#         elif number == POLAR:
#             polar_Out(n.p,ofst)
#         else:
#             print("Incorrect Number")


# In[ ]:





# In[ ]:





# In[ ]:




