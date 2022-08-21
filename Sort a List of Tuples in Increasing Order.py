#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

# In[26]:


n = int(input("Enter the size  of list :"))
print()
list1 = []
print("Enter the element of list :")
for x in range(0,n):
    m = int(input())
    list1.append(m)
print("list :",list1)
print()
tuple1 = [x for x in zip(*[iter(list1)]*2)]
print("list of tuples :",tuple1)
print()
tuple1.sort(key = lambda x: x[-1])
print("sorted element in list of tuples in increasing order by the last element :",tuple1)


# In[ ]:




