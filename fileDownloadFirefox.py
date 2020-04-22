from selenium import webdriver
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "C:\SeleniumTest")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(executable_path="C:\Drivers\FirefoxDriver\geckodriver.exe", firefox_profile=fp)
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


