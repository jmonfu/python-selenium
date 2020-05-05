from selenium import webdriver
import pytest

# to generate test and report
# pytest -v -s --html=.\Reports\report.html --self-contained-html test_Orange_hrm.py

class TestOrangeHrm():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="C:/Drivers/ChromeDriver/chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.maximize_window
        yield
        self.driver.quit()

    def test_homePageTitle(self, setup):
        assert self.driver.title == "OrangeHRM"

    def test_login(self, setup):
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title == "OrangeHRM"

if __name__ == '__main__':
    pytest.main()
