from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.expedia.com/")

driver.find_element_by_id("tab-flight-tab-hp").click()

driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("Malta")
time.sleep(2)

driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("Brussels")
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='flight-departing-hp-flight']").clear()
driver.find_element(By.XPATH, "//*[@id='flight-departing-hp-flight']").send_keys("04/15/2020")

driver.find_element(By.XPATH, "//*[@id='flight-returning-hp-flight']").clear()
driver.find_element(By.XPATH, "//*[@id='flight-returning-hp-flight']").send_keys("04/20/2020")

driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[8]/label").click()

# Explicit wait - wait for the element to be visible and clickable
wait = WebDriverWait(driver, 10)
ele = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))
ele.click()
time.sleep(3)
driver.quit()
