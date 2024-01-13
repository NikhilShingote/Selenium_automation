import time

import openpyxl
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Excel_Func import functions

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=opt)


driver.get("https://sbi.co.in/web/student-platform/maturity-value-calculator")
driver.maximize_window()

# First get the Excel file
file =  "J:\Selenium_test_data.xlsx"
rows = functions.row_count(file, "Sheet1")

for r in range(2, rows+1):
    principal = functions.read_data(file, "Sheet1", r, 1)
    Ann_rate = functions.read_data(file, "Sheet1", r, 2)
    par_1 = functions.read_data(file, "Sheet1", r, 3)
    par_2 = functions.read_data(file, "Sheet1", r, 4)
    exp_maturity = functions.read_data(file, "Sheet1", r, 5)

    # before starting clear all the fields
    driver.find_element(By.XPATH, "//*[@id='u_amount']").clear()
    driver.find_element(By.XPATH, "// *[ @ id = 'uRate']").clear()
    driver.find_element(By.XPATH, "//*[@id='uTime']").clear()
    # Passing data to application
    driver.find_element(By.XPATH, "//*[@id='u_amount']").send_keys(principal)
    time.sleep(2)
    driver.find_element(By.XPATH, "// *[ @ id = 'uRate']").send_keys(Ann_rate)
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='uTime']").send_keys(par_1)
    time.sleep(2)

    # here we need select class as we are dealing with dropdown here
    period_drp = Select(driver.find_element(By.XPATH, "//*[@id='selPeriodID']"))
    # Now from this dropdown "period_drp" we need to select the option
    period_drp.select_by_visible_text(par_2)
    time.sleep(2)
    actual_maturity = driver.find_element(By.XPATH, "//body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[2]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/p[1]/span").text
    actual_maturity = actual_maturity.replace(",", "")

    # Validation
    if float(exp_maturity) == float(actual_maturity):
        print("test Passed")
        functions.write_data(file, "Sheet1", r, 7, "Passed")

    else:
        print("test Failed")
        functions.write_data(file, "Sheet1", r, 7, "Failed")

    # Clearing the text fields after every iteration
    driver.find_element(By.XPATH, "//*[@id='u_amount']").clear()
    driver.find_element(By.XPATH, "// *[ @ id = 'uRate']").clear()
    driver.find_element(By.XPATH, "//*[@id='uTime']").clear()
    time.sleep(3)