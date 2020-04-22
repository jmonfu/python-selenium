from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "C:\SeleniumTest"})
driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe", options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

# download a text file
driver.find_element_by_xpath("//*[@id='textbox']").send_keys("Testing download text file")
driver.find_element_by_xpath("//*[@id='createTxt']").click()
driver.find_element_by_xpath("//*[@id='link-to-download']").click()

# download pdf file
driver.find_element_by_xpath("//*[@id='pdfbox']").send_keys("Testing download text file")
driver.find_element_by_xpath("//*[@id='createPdf']").click()
driver.find_element_by_xpath("//*[@id='pdf-link-to-download']").click()
