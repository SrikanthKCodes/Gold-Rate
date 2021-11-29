#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
page=requests.get("https://economictimes.indiatimes.com/commoditysummary/symbol-GOLD.cmshttps://economictimes.indiatimes.com/commoditysummary/symbol-GOLD.cms")
soup=BeautifulSoup(page.content, "html.parser")
a=soup.find_all(class_="commodityPrice")
for x in a:
    val=x.text[:]
    print(val)


# In[ ]:




