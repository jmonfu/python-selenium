from selenium import webdriver
import unittest
import HtmlTestRunner


# to generate report this test needs to run in the Terminal
# python testCase_Orange_hrm_login.py
class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Drivers\\ChromeDriver\\chromedriver.exe")
        cls.driver.maximize_window()

    def test_HomePageTitleVerification(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title does not match")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title does not match")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        # output="C:\\MyProjects_V2\\Git\\Python\\python-selenium\\htmlTestRunner\\Reports\\"))
        output=".\\Reports"))
