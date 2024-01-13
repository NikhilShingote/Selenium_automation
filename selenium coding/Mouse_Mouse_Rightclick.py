import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()


button = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/p/span")

act = ActionChains(driver)

# we need to get the method for right click
act.context_click(button).perform()
time.sleep(10)