#!/usr/bin/env python
# coding: utf-8

# In[2]:


import import_ipynb
from number import Number


# In[ ]:


class Container:
    
    def __init__(self, size):
        self.size = size
        self.length = 0
        self.max_len = 10000
        
    def con_Clear(self):
        self.length = 0
        
        
    def con_InRnd(self, file):
        with open(f"{file}.txt", "a+") as f:
            f.truncate(0)
        while self.length < self.size < self.max_len:
            self.n = Number()
            self.n.num_InRnd()
            self.n.num_In(file)
            self.length += 1
            
    
    
    def con_In(self, file):
        self.list, self.another_list = [], []
        with open(f"{file}.txt", "r+") as f:
            for line in f:
                self.list.append(float(line.strip("\n").split()[-1]))
            
    
    
    def con_Out(self, file):
        with open(f"{file}.txt", "a+") as f:
            f.truncate(0)
            f.write(f"The container contains {len(self.list)} elements \n")
            for i in range(len(self.list)):
                f.write(f"{i} : {self.list[i]} \n")
                
    
    def binary_search(self, arr, val, start, end):
        if start == end:
            if arr[start] < val:
                return start
            else:
                return start+1


        if start > end:
            return start

        mid = (start+end)//2
        if arr[mid] > val:
            return self.binary_search(arr, val, mid+1, end)
        elif arr[mid] < val:
            return self.binary_search(arr, val, start, mid-1)
        else:
            return mid
        
    def BinarySearch(self):
        arr = self.list
        for i in range(1, len(self.list)):
            val = arr[i]
            j = self.binary_search(arr, val, 0, i-1)
            arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
        self.list = arr
        return self.list


# In[ ]:




