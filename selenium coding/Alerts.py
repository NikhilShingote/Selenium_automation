from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=options)

driver.get("http://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH, "//div[@class='example']/ul/li[3]/button").click()
# driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
# here normalize-space() method is exactly equal to text method which captures inner text(in text method we exactly need to give the value)
# driver.find_element(By.XPATH, "//button[normalize-space()= 'Click for JS Prompt']").click()

# handling Alert here
# switching to alert window as alert window is not a webelement
alert_window = driver.switch_to.alert
print(alert_window.text)

# directly pass the value into alert window
alert_window.send_keys("Wow i am on alert window")

# closing the alert window
# by using OK button
# alert_window.accept()

# by using cancel button
alert_window.dismiss()