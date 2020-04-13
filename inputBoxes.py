from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# how many input boxes do we have on the web page
inputBoxes = driver.find_elements(By.CLASS_NAME, 'text_field')

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print(status)

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print(status)

# provide value inside the text box
driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("Johann")
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("Montfort")

# get status of the input box

time.sleep(2)
driver.quit()

