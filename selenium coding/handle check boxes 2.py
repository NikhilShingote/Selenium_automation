import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=options)


driver.get("https://demoqa.com/checkbox")
driver.maximize_window()

#driver.find_element(By.XPATH, "//button[@title='Toggle']//*[name()='svg']").click()
#driver.find_element(By.XPATH,"//li[2]//span[1]//button[1]//*[name()='svg']").click()
#driver.find_element(By.XPATH,"//body//div[@id='app']//li[@class='rct-node rct-node-parent rct-node-expanded']//li[@class='rct-node rct-node-parent rct-node-expanded']//li[1]//span[1]//button[1]//*[name()='svg']").click()
#driver.find_element(By.XPATH,"//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/ol/li[2]/span/label/span[1]/svg").click()

driver.find_element(By.XPATH, "//*[@class='rct-icon rct-icon-expand-close']").click()
web_elements = driver.find_elements(By.XPATH, "//button[@class='rct-collapse rct-collapse-btn']")
for x in range(len(web_elements)):
    if x == 2:
        web_elements[x].click()
web_elements1 = driver.find_elements(By.XPATH, "//button[@class='rct-collapse rct-collapse-btn']")
for x in range(len(web_elements1)):
    if x == 3:
        web_elements1[x].click()

driver.find_element(By.XPATH, "//label[@for='tree-node-angular']//span[@class='rct-checkbox']//*[name()='svg']").click()
#for x in range(len(web_elements2)):
    #if x == 5:
        #web_elements1[x].click()




