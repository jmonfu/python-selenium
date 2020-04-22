import xlUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.maximize_window()
driver.get("http://newtours.demoaut.com/")

path = "C://SeleniumTest/Login.xlsx"

rows = xlUtils.getRowCount(path, 'Sheet1')
for r in range(2,rows+1): # first row is header so avoid
    username = xlUtils.readData(path, "Sheet1", r, 1)
    password = xlUtils.readData(path, "Sheet1", r, 2)
    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()

    if driver.title == "Find a Flight: Mercury Tours:":
        print("test is passed")
        xlUtils.writeData(path, "Sheet1", r, 3, "test passed")
    else:
        print("test failed")
        xlUtils.writeData(path, "Sheet1", r, 3, "test failed")

    # now go back to home page to do the next cycle
    driver.find_element_by_link_text("Home").click()
