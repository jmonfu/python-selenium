from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

# scroll down the page by pixels
# driver.execute_script("window.scrollTo(0, 1000)")

# scroll down the page until element visible (in our case find Vatican City)
# searchedEle = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[101]/td[2]")
# driver.execute_script("arguments[0].scrollIntoView();", searchedEle)

# scroll down till the end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(5)
driver.quit()
