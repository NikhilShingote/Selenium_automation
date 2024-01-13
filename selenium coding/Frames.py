from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:\Drivers\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

# You can search for "iframe" in HTML code you will get frame webelement
# You can pass "Name of the frame", "Id of the frame", or "Webelement" inside the frame method
# You can get various tag names for frames e.g. frames,iframes,form.
# We need to switch to 1st frame then to 2nd frame
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
# go back to main page
# since we cannot directly switch to next frame, we need to go back to the main default page and then go to 2nd frame
driver.switch_to.default_content()

# switch to 2nd frame
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
# go back to main page
driver.switch_to.default_content()


# switch to 3rd frame
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()
time.sleep(3)