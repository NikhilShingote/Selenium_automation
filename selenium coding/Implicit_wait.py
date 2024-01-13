from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# Implicit wait
driver.implicitly_wait(10)

driver.get("https://www.adidas.com/us")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@class='_input_1f3oz_13']").send_keys("shoes")
driver.find_element(By.XPATH, "//div[@class='_icon_1f3oz_44']//span[@role='img']").click()


