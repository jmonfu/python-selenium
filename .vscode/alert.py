from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)

# driver.switch_to_alert().accept()  # closes the alert window by pressing the OK button
driver.switch_to_alert().dismiss()  # closes the alert window by pressing the CANCEL button