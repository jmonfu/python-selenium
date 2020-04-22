from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
driver.get("https://amazon.co.uk/")
driver.maximize_window()

# capture all cookies created by the browser
cookies = driver.get_cookies()
noOfCookies = len(cookies)
print(noOfCookies)

# adding new cookie to the browser
cookie = {'name': 'MyCookie', 'value': '1234567'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
noOfCookies = len(cookies)
print(noOfCookies)

# delete cookie from the browser
driver.delete_cookie('MyCookie')

cookies = driver.get_cookies()
noOfCookies = len(cookies)
print(noOfCookies)

driver.quit()