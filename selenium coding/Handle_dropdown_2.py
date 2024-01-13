from selenium import webdriver
from selenium.webdriver.common.by import By                         # for getting 0element
from selenium.webdriver.chrome.service import Service               # for Driver address
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=options)

driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Dropdown").click()

element = driver.find_element(By.XPATH,"//select[@id='dropdown']")
drop_down = Select(element)

#drop_down.select_by_visible_text("Option 2")
#drop_down.select_by_value("1")
drop_down.select_by_index(2)