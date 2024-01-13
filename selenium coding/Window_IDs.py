import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(7)
driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()

# Approach 1
# here we are focusing on our main window
# Means we are getting our single window ID here
window_id = driver.current_window_handle
print(window_id)

# Here we are getting window ids of all the windows that are open
# So we can shift our focus on multiple windows
window_IDs = driver.window_handles
parent_window_id = window_IDs[0]
child_window_id = window_IDs[1]
print(type(window_IDs))

driver.switch_to.window(child_window_id)
print("Title of child window", driver.title)

driver.switch_to.window(parent_window_id)
print("Title of parent window", driver.title)

# Approach 2
# you can also put this in for loop instead of writing all the IDs in a different variables
for win_id in window_IDs:
    driver.switch_to.window(win_id)
    if driver.title == "OrangeHRM":
        driver.close()

# here we are trying to close a specific browser window with the help of title
