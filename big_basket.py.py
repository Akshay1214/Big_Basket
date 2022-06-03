#!/usr/bin/env python
# coding: utf-8

# In[23]:


from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import time
import openpyxl

driver = webdriver.Chrome()
driver.get("https://www.bigbasket.com/")
driver.maximize_window()


category = driver.find_element(by=By.XPATH, value='//*[@id="store-entry"]/div[1]/div/div[4]/div/div/a')
category.click()
time.sleep(2)

product_name = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[1]/a ')
product_mrp = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[3]/div/div[1]/h4/span[2]')
product_wt = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[2]/div/span/button/span/span[1]')

name, mrp, wt = [],[],[]

for x in product_name:
    name.append(x.text)
for y in product_mrp:
    mrp.append(y.text)
for z in product_wt:
    wt.append(z.text)


'''
//*[@id="store-entry"]/div[1]/div/div[4]/div/div/a/img
//*[@qa="product_name"]
//*[@class="ng-binding"][3]



'''


# In[24]:


print(len(name), len(mrp), len(wt))


# In[35]:


final_sheet = zip(name, mrp, wt)


# In[38]:


print(final_sheet)


# In[36]:


wb = openpyxl.Workbook()
sheet = wb.active
for i in list(final_sheet):
    sheet.append(i)
    wb.save("Ayurved_Data.csv")


# In[33]:


b = {"Product Name":name, "Product Price":mrp, "Product Weight/Quantity":wt}
df = pd.DataFrame(b)
df = pd.DataFrame.from_dict(b, orient='index')
df = df.transpose()
#df = b.ffill(axis=None, inplace=False, limit=None, downcast=None)
#df = df.transpose()

driver.quit()


# In[ ]:




