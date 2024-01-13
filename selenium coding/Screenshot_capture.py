import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options= opt)


driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# How to capture screenshot of webpage
# Here copy the file path where you want to save and give any name e.g. we have given "homepage"
# Method_1
driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\Selenium_automation\\selenium coding\\homepage.png")

# Method_2
# We import os class here
driver.save_screenshot(os.getcwd()+"\\homepage.png")

# Method_3
# driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")

driver.quit()