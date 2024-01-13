from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)


service_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=options)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

# here a frame is present inside a frame
# so we dont need to go to default frame
driver.find_element(By.XPATH,"//a[contains(normalize-space(),'Iframe with in an Iframe')]").click()

# here we are using webelement in frame() method instead of name or id as we dont find name or id in iframe tag
outer_frame = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)

inner_frame = driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(inner_frame)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Hello Brother")