from selenium import webdriver
from selenium.webdriver.common.by import By                         # for getting element
from selenium.webdriver.chrome.service import Service


serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

email_box = driver.find_element(By.XPATH,"//input[@id='Email']")
email_box.clear()
email_box.send_keys("abc@gmail.com")

login = driver.find_element(By.XPATH,"//button[@type='submit']")

print("result of text: ",email_box.text)  # "text" returns inner text
print("result of get attribute: ",email_box.get_attribute('value')) # gets "value" of any attribute of web element

print("result of text: ",login.text)
print("result of get attribute: ",login.get_attribute('type'))  # gets "type" of any attribute