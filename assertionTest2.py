import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testIsTitleTrue(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
        driver.get("https://www.google.com")
        titleOfWebPage = driver.title
        self.assertTrue(titleOfWebPage == "Google", "title is True")

    def testIsTitleFalse(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
        driver.get("https://www.google.com")
        titleOfWebPage = driver.title
        self.assertFalse(titleOfWebPage == "Goooooooooogle", "title is False")


if __name__ == '__main__':
    unittest.main
