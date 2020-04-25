import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testIsTitleTrue(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver.exe")
        # driver = None
        # self.assertIsNone(driver)
        self.assertIsNotNone(driver)

if __name__ == '__main__':
    unittest.main
