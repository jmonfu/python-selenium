from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# dropdown select
drp = Select(driver.find_element_by_id("RESULT_RadioButton-9"))
drp.select_by_visible_text('Morning')
time.sleep(2)
drp.select_by_index(2)
time.sleep(2)
drp.select_by_value('Radio-2')

# count number of options
print(len(drp.options))

# capture all options and print them out
all_options = drp.options
for option in all_options:
    print(option.text)

driver.quit()