
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=opt)


driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

'''Method_1'''
# ctrl + Enter keys opens a new tab so we are using that method
# RETURN = ENTER key
# driver.find_element(By.LINK_TEXT, "Register").send_keys(Keys.CONTROL+Keys.RETURN)

''' Method_2
In Selenium 4 new functionality is added
It opens a new tab and automatically switches to new tab'''

# New Tab
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('tab')             # This new command in selenium 4 opens a new tab and shifts focus to it.
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

# New Window
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window')             # This new command in selenium 4 opens a new window and shifts focus to it.
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")