from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Accessing title of webpage
# This are actually variables which are accessed by driver instance
print(driver.title)

# getting current url
print(driver.current_url)

# Page source
# print(driver.page_source)