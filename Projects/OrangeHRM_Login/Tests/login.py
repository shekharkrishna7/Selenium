from selenium import webdriver
import unittest
import time
from OrangeHRM_Login.Pages.loginPage import LoginPage
from OrangeHRM_Login.Pages.homePage import HomePage


# import pandas as pd
#
# Login_credentials = pd.read_csv("")


class LoginTest(unittest.TestCase):
    browser_profile = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.browser_profile = webdriver.ChromeOptions().add_experimental_option('prefs', {
            'intl.accept_languages': 'en,en_US'})
        cls.driver = webdriver.Chrome(r"E:\SK_Learning\Web Scraping\Selenium\Projects\chromedriver.exe",
                                      options=cls.browser_profile)
        cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()

    def test_login_valid_un_valid_pw(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        login = LoginPage(driver)
        login.enter_username("admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        time.sleep(5)
        homepage.click_logout()

    def test_login_valid_un_invalid_pw(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        login = LoginPage(driver)
        login.enter_username("admin")
        login.enter_password("admin")
        login.click_login()
        time.sleep(2)
        assert "Invalid" in login.invalid_credential_text(), "Invalid Credentials Assertion Failed"

    def test_login_invalid_un_valid_pw(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        login = LoginPage(driver)
        login.enter_username("admi")
        login.enter_password("admin123")
        login.click_login()
        time.sleep(4)
        print(login.invalid_credential_text())
        assert "Invalid" in login.invalid_credential_text(), "Invalid Credentials Assertion Failed"

    def test_login_invalid_un_invalid_pw(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        login = LoginPage(driver)
        login.enter_username("admi")
        login.enter_password("admi")
        login.click_login()
        time.sleep(3)
        assert "Invalid" in login.invalid_credential_text(), "Invalid Credentials Assertion Failed"

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == 'main':
    unittest.main()
