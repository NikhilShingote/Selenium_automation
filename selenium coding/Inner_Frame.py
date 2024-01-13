from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

# web element for button
driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

# identify outer iframe
outer_iframe = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
# outer_iframe is a webelement
# switch to outer frame
driver.switch_to.frame(outer_iframe)


# identify inner iframe
inner_iframe = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
# inner_iframe is a web element
# switch to inner frame
driver.switch_to.frame(inner_iframe)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcome")