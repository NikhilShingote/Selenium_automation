# Here we need to install the request package for broken links through settings -> python interpreter -> requests
import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME,'a')
count = 0
for link in links:
    url = link.get_attribute('href')
    # while working with the urls there are some exceptions thrown to avoid this we use try except
    # hit thr request URL
    try:
        response = requests.head(url)
    except:
        None
    if response.status_code>=400:
        print(url," is broken link")
        count+=1
    else:
        print(url, " is valid link")
print("Total no of broken links: ",count)