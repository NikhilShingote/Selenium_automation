from selenium import webdriver
from selenium.webdriver.common.by import By                         # for getting element
from selenium.webdriver.chrome.service import Service


serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.snapdeal.com")
driver.maximize_window()
# 1.
# find element - returns single web element
# driver.find_element(By.XPATH,"//input[@id='inputValEnter']").send_keys("shoes")

# 2.
# locators with multiple webelments but we are using findelement
# text_element = driver.find_element(By.XPATH, "//div[@class='middleTop row']//a")
# print(text_element.text)

# find elements
# 1.
# find elements - returns single web element
# elements = driver.find_elements(By.XPATH,"//input[@id='inputValEnter']")
# print(len(elements))

# 2.
# find elements
text_elements = driver.find_elements(By.XPATH, "//div[@class='middleTop row']//a")
print(len(text_elements))
for x in text_elements:
    print(x.text)


