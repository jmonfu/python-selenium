from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle) # CDwindow-11B4BCB4CDB71BBFB0E7EDFE28405584 - parent window

handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    time.sleep(5)
    if driver.title == "Frames & windows":
        driver.close()
        time.sleep(2)

time.sleep(2)
driver.quit()
