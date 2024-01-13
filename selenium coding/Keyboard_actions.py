import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=options)


driver.get("https://text-compare.com/")
driver.maximize_window()

input_1 = driver.find_element(By.XPATH, "//*[@id='inputText1']")
input_2 = driver.find_element(By.XPATH, "//*[@id='inputText2']")

input_1.send_keys("Welcome")

# Now for keyword actions

act = ActionChains(driver)

# Input_1 ctrl+A to select the text
act.key_down(Keys.CONTROL)   # this will press the control key
act.send_keys("a")
act.key_up(Keys.CONTROL)    # for releasing the control key
act.perform()

# input_1 ctrl+C to copy
act.key_down(Keys.CONTROL)      # this will press the control key
act.send_keys("c")
act.key_up(Keys.CONTROL)        # for releasing the control key
act.perform()

# Input_2 press tab key to navigate
act.send_keys(Keys.TAB).perform()

# Input_2 Ctrl+V to paste
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()