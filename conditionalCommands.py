from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

eleUserName = driver.find_element_by_name("userName")
print(eleUserName.is_displayed())
print(eleUserName.is_enabled())

elePassword = driver.find_element_by_name("password")

eleUserName.send_keys("mercury")
elePassword.send_keys("mercury")

driver.find_element_by_name("login").click()

# verify that we have infact logged in

roundTrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
oneWay_radio = driver.find_element_by_css_selector("input[value=oneway]")
print("status of round trip radio button", roundTrip_radio.is_selected())
print("status of one way radio button", oneWay_radio.is_selected())

time.sleep(5)
driver.quit()

