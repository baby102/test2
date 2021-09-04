import time
import pytest
from selenium import webdriver

class Test_Login:
    def setup(self):
        chrome_capabilities = {
            "browserName": "firefox",
            "version": "",
            "platform": "ANY",
            "javascriptEnabled": True,
            # "marionette": True,
        }
        self.driver = webdriver.Remote("http://192.168.3.27:4444/wd/hub", desired_capabilities=chrome_capabilities)
        self.driver.implicitly_wait(2)

    def test_1(self):
        self.driver.get("http://www.163.com")
        time.sleep(3)
        self.driver.quit()



    def test_2(self):
        self.driver.get("http://www.163.com")
        time.sleep(3)
        self.driver.quit()

    def test_3(self):
        self.driver.get("http://www.163.com")
        time.sleep(3)
        self.driver.quit()

    def test_4(self):
        self.driver.get("http://www.163.com")
        time.sleep(3)
        self.driver.quit()


    def test_5(self):
        self.driver.get("http://www.163.com")
        time.sleep(3)
        self.driver.quit()

    def test_6(self):
        self.driver.get("http://www.163.com")
        time.sleep(3)
        self.driver.quit()

    def test_7(self):
        self.driver.get("http://www.163.com")
        time.sleep(3)
        self.driver.quit()

    def test_8(self):
        self.driver.get("http://www.163.com")
        time.sleep(3)
        self.driver.quit()

    def test_9(self):
        self.driver.get("http://www.163.com")
        time.sleep(3)
        self.driver.quit()

    def test_10(self):
        self.driver.get("http://www.163.com")
        time.sleep(3)
        self.driver.quit()

    def test_11(self):
        self.driver.get("http://www.163.com")
        time.sleep(3)
        self.driver.quit()

    def test_12(self):
        self.driver.get("http://www.163.com")
        time.sleep(3)
        self.driver.quit()
