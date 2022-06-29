#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
import io

r = requests.get("http://localhost:9000/exp?query=select * from  BitCoinPrice")
rawData = r.text
print(rawData)


# In[10]:


import pandas as pd

pData = pd.read_csv(io.StringIO(rawData), parse_dates=['Priceat'])
print(pData)


# In[11]:


from matplotlib import pyplot as plt

pData.plot("Priceat", ["value"], subplots=True)


# In[ ]:




