import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

mywait = WebDriverWait(driver,5)


driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
# time.sleep(2)
y = mywait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='wikipedia-search-results']/div/a")))
for i in y:
    x = i.click()

# capture windowid of every browser window
# based on window id switch to each browser window, capture the title of every browser window and print
wind_ids = driver.window_handles

# switching focus to window
for c in wind_ids:
    driver.switch_to.window(c)
    print("Title of window: ",driver.title)

driver.quit()

