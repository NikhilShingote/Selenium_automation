from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=options)

#Now since this alert windows are not webelements and not a part of the application
#so in this alert we need to pass the username and password which we cannot do directly by getting webelement or by using switch to alert commands
#so we have to pass the username and password in URL itself
# syntax - http://{Username:password@}{URL}

driver.get("http://admin:admin@the-internet.herokuapp.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Basic Auth").click()


