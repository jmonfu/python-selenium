from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()

ele = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)
actions.double_click(ele).click().perform()

time.sleep(5)
driver.quit()
