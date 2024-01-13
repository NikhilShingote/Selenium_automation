import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# For Chrome Browser functions
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Drivers\chromedriver.exe")
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=serv_obj, options=opt)
    return driver


driver1 = chrome_setup()
driver1.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver1.maximize_window()

# As there is an exception of Element click intercepted we need to handle this exception by scrolling down
# scroll down till the element
flag = driver1.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]")
driver1.execute_script("arguments[0].scrollIntoView();",flag)
value = driver1.execute_script("return window.pageYOffset;")
print("Number of pixels",value)

# def edge_setup():
#     from selenium.webdriver.edge.service import Service
#     serv_obj = Service("C:\Drivers\msedgedriver.exe")
#     opt = webdriver.EdgeOptions()
#     opt.add_experimental_option('detach', True)
#     driver = webdriver.Edge(service=serv_obj, options=opt)
#     return driver
#
#
# # Here the driver variable is getting the return driver value from the function
# # driver = chrome_setup()
# driver = edge_setup()
# driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# driver.maximize_window()
# driver.execute_script(
#     "window.scrollTo(0, 200)")  # To scroll down as it was not able to find the webelement and click on it.
# time.sleep(5)
# driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()
