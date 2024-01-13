# This pop ups are different from application popups because this are browser popups which cannot be handled directly nor it can be bypassed.
# So we need browser level setting to disable those notifications.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Creating object
obj = webdriver.ChromeOptions()

# We need the method from ChromeOptions class
# we need to pass the parameter
obj.add_argument("--disable-notification")
serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=obj)     # Launched the browser and disable the notification popup

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
