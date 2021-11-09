#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import random
import import_ipynb
from container import Container


# In[5]:


class Main:
    
    def __init__(self, argc, argv):
        self.argc = argc
        start_time = time.time()
#         argc = int(argv.split()[2])
        if  self.argc <= 5: # no of operations
            self.errMessage1()
            return
        elif self.argc >=5 and self.argc <= 10000:
            print("Start")
            c = Container(self.argc)
            c.con_Clear()
            if argv.split()[1] == "-f":
                c.con_InRnd(argv.split()[-2])
            elif argv.split()[1] == "-n":
                c.con_In(argv.split()[-2])
                c.BinarySearch()
                c.con_Out(argv.split()[-1])    
            end_time = time.time()
            print("Time taken :", end_time - start_time)
            print("End")
        else:
            self.errMessage2()
            return
         
        
    def errMessage1(self):
        print("Incorrect command line! \n Waited: \n command -f infile outflie01 outfile02 \n Or:\n command -n number outfile01 outfile02 \n")
    
    def errMessage2(self):
        print("Incorrect qualifier vaalue! \n Waited: \n command -f infile outflie01 outfile02 \n Or:\n command -n number outfile01 outfile02 \n")  


# In[18]:


Main(1000, "command -f infile outfile31 outfile32")


# In[19]:


Main(1000, "command -n 100 outfile31 outfile32")


# In[ ]:





# In[ ]:


# command -n 6 outfile01 outfile02

