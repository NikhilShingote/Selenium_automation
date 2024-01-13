import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# To capture a webelement which will capture all the checboxes
# Now store all the checkboxes into a available List variable
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")

# Approach 1
# For checking all the checkboxes
#for i in range(len(checkboxes)):
#    checkboxes[i].click()

# Approach 2
#for checkbox in checkboxes:
    #checkbox.click()


# Selecting checkboxes by choice
#for checkbox in checkboxes:
    # For getting attribute value we use
    #day = checkbox.get_attribute('id')
    #if day in ['monday','sunday', 'wednesday']:
        #checkbox.click()

# Selecting last 2 checkboxes
for i in range(len(checkboxes) - 2, len(checkboxes)):
    checkboxes[i].click()
# How to uncheck the checkbox
# How will we know if checkbox is selected or not
#for checkbox in checkboxes:
   # if checkbox.is_selected():
     #   checkbox.click()