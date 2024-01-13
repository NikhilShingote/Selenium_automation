from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# to check if element is present on webpage
# it gives boolean value
# this methods are accessed through webelements and not through driver
searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Status is: ",searchbox.is_displayed())

# to check is element is enabled
print("Status is: ",searchbox.is_enabled())

# TO CHECK IF RADIO button/CHECK BOX is selected or not
radiobtn_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
radiobtn_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

#check status
print(radiobtn_male.is_selected())
print(radiobtn_female.is_selected())

# Now lets click the radio buton and check the status
radiobtn_male.click()

#check status again
print(radiobtn_male.is_selected())
print(radiobtn_female.is_selected())