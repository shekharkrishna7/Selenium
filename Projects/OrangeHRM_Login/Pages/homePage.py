from selenium.webdriver.common.by import By
from OrangeHRM_Login.Locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_welcome(self):
        self.driver.find_element(By.ID, Locators.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, Locators.logout_link_linkText).click()


