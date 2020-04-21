import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class CMS_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/users/krish/OneDrive/Documents/GitHub/CMS_Clients1/tests/chromedriver_win32/chromedriver')

    def test_cms(self):
        user = "Krishna"
        pwd = "django123"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://europescorner.pythonanywhere.com/")
        elem = driver.find_element_by_xpath("//*[@id='navbarCollapse']/form/a[1]").click()
        time.sleep(3)

        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        try:
            # attempt to find the '+ New' - if found, logged in
            elem = driver.find_element_by_xpath("/html/body/div[1]/nav/a[2]/i").click()
            elem = driver.find_element_by_xpath("/html/body/div[2]/h1")
            assert True

        except NoSuchElementException:
            self.fail("Cart failed")
            assert False

        time.sleep(3)

def tearDown(self):
    self.driver.close()

if __name__ == '__main__':
    unittest.main()
