import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=options)

mywait = WebDriverWait(driver,10)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

element = mywait.until(EC.presence_of_element_located((By.NAME, "username")))
element.send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

webelement1 = mywait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='oxd-main-menu']/li[1]/a")))
webelement1.click()
webelement2 = mywait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='User Management']")))
webelement2.click()
webelement3 = mywait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='oxd-dropdown-menu']//li")))
webelement3.click()

x = mywait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div")))
y = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body oxd-card-table-body']/div/div/div/div[2]/div[3]/div/div[2]")
# for i in range(1,len(x)+1):
#     ele = driver.find_element(By.XPATH, "//div[@class='oxd-table-body oxd-card-table-body']/div["+str(i)+"]/div/div/div[2]/div[3]/div/div[2]").text
#     print(ele)
# //div[@class='oxd-table-body oxd-card-table-body']/div[2]/div/div/div[2]/div[3]/div/div[2]
print(len(x))
print(len(y))
