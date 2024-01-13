import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.w3schools.com/TAGS/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

# Now to switch to the frame
driver.switch_to.frame("iframeResult")

field1 = driver.find_element(By.XPATH, "//*[@id='field1']")
field1.clear()
field1.send_keys("welcome")

button = driver.find_element(By.XPATH, "/html/body/button")

# Mouse Actions
act = ActionChains(driver)

# we need to access the double click method from Actionchains class
act.double_click(button).perform()
time.sleep(10)