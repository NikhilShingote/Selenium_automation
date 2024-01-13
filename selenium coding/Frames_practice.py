from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver.exe")
opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=serv_obj, options=opt)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.XPATH, "//*[@id='tinymce']").clear()
driver.find_element(By.XPATH, "//*[@id='tinymce']").send_keys("I am here now")