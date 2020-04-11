# taken from the youtube series https://www.youtube.com/watch?v=0eeq0A6rc_E&list=PLUDwpEzHYYLvx6SuogA7Zhb_hZl3sln66
# &index=6

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\Drivers\FirefoxDriver\geckodriver.exe")
driver = webdriver.Edge(executable_path="C:\Drivers\EdgeDriver\msedgedriver.exe")

driver.get("http://newtours.demoaut.com/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()
