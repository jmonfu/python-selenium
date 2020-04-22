from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

ele = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

actions = ActionChains(driver)
actions.context_click(ele).perform()


time.sleep(5)
driver.quit()