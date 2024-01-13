# 1. Count no. of rows and columns in a table.
# 2. read specific row and column data
# 3. Read all rows and columns
# 4. read data on certain conditions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1. Count no. of rows and columns in a table.

web_elements_1= driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
no_of_rows = len(web_elements_1)


web_elements_2 = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th")
no_of_columns = len(web_elements_2)

print(no_of_rows)
print(no_of_columns)

# 2. read specific row and column data
web_elements_3 = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]")
print(web_elements_3.text)

# 3. Read all rows and columns
for row in range(1,no_of_rows+1):
    for column in range(1,no_of_columns+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(row)+"]/td["+str(column)+"]").text
        print(data, end="")
    print()

# 4. read data on certain conditions
# list book names whose author is mukesh
for row in range(1, no_of_rows+1):
    author_name = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]/td[2]").text
    if author_name == "Mukesh":
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]/td[1]").text
        print(author_name," is the author of book",book_name)


