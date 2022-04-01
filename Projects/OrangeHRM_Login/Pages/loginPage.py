from selenium.webdriver.common.by import By
from OrangeHRM_Login.Locators.locators import Locators
# from selenium import  webdriver


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, Locators.username_textbox_id).clear()
        self.driver.find_element(By.ID, Locators.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, Locators.password_textbox_id).clear()
        self.driver.find_element(By.ID, Locators.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, Locators.login_button_id).click()

    def invalid_credential_text(self):
        assertion_text = self.driver.find_element(By.XPATH, Locators.invalid_credential_text_id).text
        return assertion_text
