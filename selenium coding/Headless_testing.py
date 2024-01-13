from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('detach', True)
    opt.add_argument('--headless')
    serv_obj = Service("C:\Drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj, options=opt)
    return driver

driver = headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.quit()