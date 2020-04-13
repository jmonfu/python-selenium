from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# radio buttons

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

element = driver.find_element_by_id("RESULT_RadioButton-7_0")
webdriver.ActionChains(driver).move_to_element(element).click(element).perform()

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

# checkboxes
status = driver.find_element_by_id("RESULT_CheckBox-8_0").is_selected()
print(status)

element = driver.find_element_by_id("RESULT_CheckBox-8_0")
webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
status = driver.find_element_by_id("RESULT_CheckBox-8_0").is_selected()
print(status)

time.sleep(2)

driver.quit()