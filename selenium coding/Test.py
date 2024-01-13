from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:/Drivers/chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("http://localhost:8888/notebooks/Untitled.ipynb?kernel_name=python3")
elements_list = driver.find_element(By.XPATH, "//*[@id='ipython_notebook']")
print(elements_list.text)