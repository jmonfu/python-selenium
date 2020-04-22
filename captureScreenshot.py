from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.get("http://newtours.demoaut.com/mercurywelcome.php")
driver.maximize_window()

driver.save_screenshot("C:\\SeleniumTest\\newtours.jpg")
driver.get_screenshot_as_file("C:\\SeleniumTest\\newtours2.png")
driver.quit()