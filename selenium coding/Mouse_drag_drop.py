import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

# here we will decide the source and target element
source_element = driver.find_element(By.ID, "box2")
target_element = driver.find_element(By.ID, "box106")

act = ActionChains(driver)

# we need to specify source and target element in the method
act.drag_and_drop(source_element, target_element).perform()
time.sleep(5)