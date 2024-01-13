from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.snapdeal.com/")
driver.maximize_window()
driver.get("https://www.amazon.com/")

# Back command
driver.back()

# forward command
driver.forward()

# refresh page
driver.refresh()