import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=options)

driver.get("http://the-internet.herokuapp.com/abtest")
driver.maximize_window()

# here we use switch_to() command to switch to other windows and pass window id in it
# Window id is generated everytime a window is opened and is different everytime
# - Current window handle gives window id of single window at a time
# - window handles gives window id of multiple windows

# to get window id
window_id = driver.current_window_handle

driver.find_element(By.LINK_TEXT,"Elemental Selenium").click()

# to get window ids of multiple window ids
# this is a list
wind_ids = driver.window_handles

first_window_id = wind_ids[0]
second_window_id = wind_ids[1]

# switching focus to 2nd window
driver.switch_to.window(second_window_id)
print("Title of 2nd window: ",driver.title)

driver.switch_to.window(first_window_id)
print("Title of 1st window: ",driver.title)

# You can also use for loop to switch between broser windows

# if you want to close specific browser window
time.sleep(3)
for win_id in wind_ids:
    driver.switch_to.window(win_id)
    if driver.title == "The Internet":
        driver.close()