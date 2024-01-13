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

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

year = "2022"
month = "May"
date = "12"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()   # Opens datepicker

# first focus on Month and Year
# Here we need to match the month and year so we will have to use while loop till the condition satisfies
while True:
    Month = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    Year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if month == Month and year == Year:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click() # for previous dates
        # driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()  # for future dates

Dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in Dates:
    if ele.text == date:
        ele.click()
        break