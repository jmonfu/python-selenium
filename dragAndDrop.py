from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

romeEle = driver.find_element_by_xpath("//*[@id='box6']")
italyEle = driver.find_element_by_xpath("//*[@id='box106']")

actions = ActionChains(driver)
actions.drag_and_drop(romeEle, italyEle).perform()
