# from selenium package we have imported webdriver module
# All the web elements are present inside the body
# absolute/full xpath starts from the root node
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:\Drivers\chromedriver.exe")

# here we created an object for chrome class so we can access all methods from chrome class
# the chrome class has a constructor which expects the location of the driver.
# this will launch the browser
driver = webdriver.Chrome(service=serv_obj)

# # this will launch the website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element(By.CLASS_NAME,"oxd-input oxd-input--active").send_keys("Admin")
driver.find_element(By.CLASS_NAME,"oxd-input oxd-input--active").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login test passed")
else:
    print("Login test Failed")

# closes the browser
driver.close()