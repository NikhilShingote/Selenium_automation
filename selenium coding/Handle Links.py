from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT,'A/B Testing').click()
# driver.find_element(By.PARTIAL_LINK_TEXT,'A/B Test').click()

# Find number of links in a page
links = driver.find_elements(By.XPATH,'//a')
print("Total no of links: ", len(links))


