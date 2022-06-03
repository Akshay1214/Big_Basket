from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("//india.eclerx.com/ctrxdata/ARRDATA/Akshay.Deokar/Desktop/Re/chromedriver.exe")
driver.get("https://www.bigbasket.com/")
driver.maximize_window()


category = driver.find_element(by=By.XPATH, value='//*[@id="store-entry"]/div[1]/div/div[4]/div/div/a')
category.click()
time.sleep(2)

product_name = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[1]/a ')
product_mrp = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[3]/div/div[1]/h4/span[2]')
product_wt = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[2]/div/span/button/span/span[1]')

name, mrp, wt = [],[],[]

for name in product_name:
    name.append(product_name.text)
for mrp in product_mrp:
    mrp.append(product_mrp.text)
for wt in product_wt:
    wt.append(product_wt.text)

d = {"Product Name":name, "Product Price":mrp, "Product Weight/Quantity":wt}
df = pd.DataFrame(d)
df

driver.quit()
'''
//*[@id="store-entry"]/div[1]/div/div[4]/div/div/a/img
//*[@qa="product_name"]
//*[@class="ng-binding"][3]



'''