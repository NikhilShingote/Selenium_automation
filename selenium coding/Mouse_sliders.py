import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

first_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
second_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

print("Location of sliders before moving")
print(first_slider.location)
print(second_slider.location)

# This location returns dictionary object with key and values
# Now we need to move the slider positions

act = ActionChains(driver)

act.drag_and_drop_by_offset(first_slider, 100,0).perform()
act.drag_and_drop_by_offset(second_slider, -100,0).perform()
time.sleep(5)

print("Location of sliders After moving")
print(first_slider.location)
print(second_slider.location)