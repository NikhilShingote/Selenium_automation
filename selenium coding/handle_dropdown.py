import time
from selenium import webdriver
from selenium.webdriver.common.by import By                         # for getting 0element
from selenium.webdriver.chrome.service import Service               # for Driver address
from selenium.webdriver.support.ui import Select                    # For dropdowns
from selenium.webdriver.support.wait import WebDriverWait           # for explicitly wait
from selenium.webdriver.support import expected_conditions as EC    # For explicitly wait

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

# Creating object for wait
# whenever you want to use explicitly wait we need to use the object
my_wait = WebDriverWait(driver, 10)

dropdown_element = my_wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='input-country']")))

# Passing web element in Select class
dropdown = Select(dropdown_element)

dropdown.select_by_visible_text("Haiti")
