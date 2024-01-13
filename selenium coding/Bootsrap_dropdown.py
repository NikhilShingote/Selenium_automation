import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('detach', True)

    serv_obj = Service("C:\Drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj, options= opt)


    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='select2-billing_country-container']").click()

countries_list = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']//li")

print(len(countries_list))

for country in countries_list:
    if country.text == "India":
        country.click()
        break

