import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testIsTitleEqual(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
        driver.get("https://www.google.com")
        titleOfWebPage = driver.title
        self.assertEqual("Google", titleOfWebPage, "title is not the same")


    def testIsTitleNotEqual(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
        driver.get("https://www.google.com")
        titleOfWebPage = driver.title
        self.assertNotEqual("Google123", titleOfWebPage, "title is the same")


if __name__ == '__main__':
    unittest.main


