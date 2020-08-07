#!/usr/bin/env python
# coding: utf-8

# In[4]:


#The below program gives the factorial of the numner entered


# In[5]:


print("This program gives the factorial of the numner entered")


# In[18]:


a = int(input("Enter the number for which the factorial is to be displayed: "))
a
product = 1


# In[19]:


for i in range(1,5):
    product = product * a
    a = a-1


# In[20]:


product


# In[21]:


print("The factorial of the entered number is", product) 


# In[ ]:




