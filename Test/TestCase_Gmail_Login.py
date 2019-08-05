from selenium import webdriver
import unittest
import HtmlTestRunner
import time
 #from SampleTest1.PomProject.page.userlogin import UserLogin

#unit testing
class GmailSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.driver=webdriver.Chrome(executable_path="/Users/macbookpro/Work/PythonProjectAutomation/SampleTest1/driver/drivers/chromedriver 2")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(4)
    # def test_login_page(self):
    #     self.driver.get("https://accounts.google.com")
    #     #self.assertEqual("Sign in – Google accounts", self.driver.title, "its not maching")
    #

    def test_username_valid(self):
        # driver = self.driver
        self.driver.get("https://accounts.google.com")
        # login = ogin_page(driver)
        # login.user_name
        # login.passwords
        # login.click()
        #

        self.driver.find_element_by_id("identifierId").send_keys("aloksoni0501@gmail.com")
        self.driver.find_element_by_xpath("//span[@class='CwaK9']").click()

        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("alok@123")
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[ text()='Next']").click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("the browser close")


if __name__=='__main__':
    unittest.main()