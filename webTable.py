from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")

rowElements = driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr")
rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
print(rowElements)
print(rows)

columnElements = driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th")
cols = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))
print(columnElements)
print(cols)

for r in range(2, rows+1):
    for c in range(1, cols+1):
        value = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end='    ')
    print()
    
driver.quit()

