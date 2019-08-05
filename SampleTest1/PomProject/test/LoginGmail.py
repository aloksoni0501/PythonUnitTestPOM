from selenium import webdriver


import unittest
import HtmlTestRunner

#from selenium.webdriver.chrome.webdriver import WebDriver
class LoginGmail(unittest.TestCase):


def setUpClass(self):
self.driver = webdriver.Chrome("/Users/macbookpro/Work/PythonProjectAutomation/SampleTest1/driver/drivers/chromedriver 2")
driver.implicitly_wait(5)
driver.maximize_window()
def login_test_valid(self):
self.driver.get("https://www.gmail.com")
driver.get("https://www.gmail.com")
driver.find_element_by_id("identifierId").send_keys("aloksoni0501@gmail.com")
driver.find_element_by_xpath("//span[@class='CwaK9']").click()

    #def tearDown(self) -> None:
driver.close()