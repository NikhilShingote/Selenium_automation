from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummies.com/article/academics-the-arts/math/statistics/how-to-find-t-values-for-confidence-intervals-169841/")
driver.maximize_window()
time.sleep(4)

# Self
# text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Buy On Amazon')]/self::a").text
# print(text_msg)

# Parent
# text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Buy On Amazon')]/parent::div").text
# print(text_msg)

# Ancestor
# ancestor = driver.find_elements(By.XPATH,"//a[contains(text(),'Buy On Amazon')]/ancestor::*")
# print(len(ancestor))

childs = driver.find_elements(By.XPATH,"//a[contains(text(),'Buy On Amazon')]/ancestor::*/child::*")
print(len(childs))