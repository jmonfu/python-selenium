from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()

driver.switch_to_frame(0)

driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C://SeleniumTest//user.png")
# driver.find_element_by_xpath("//*[@id='RESULT_FileUpload-10']").send_keys("C://SeleniumTest//user.png")
actions = ActionChains(driver)
