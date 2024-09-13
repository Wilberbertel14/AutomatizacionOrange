from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.XPATH, "//input[@placeholder='Username']")
        self.password_field = (By.XPATH, "//input[@placeholder='Password']")
        self.login_button = (By.XPATH, "//button[normalize-space()='Login']")

    def enter_username(self, username: str):
        username_element = self.wait_for_element(self.username_field)
        username_element.clear()
        username_element.send_keys(username)

    def enter_password(self, password: str):
        password_element = self.wait_for_element(self.password_field)
        password_element.clear()
        password_element.send_keys(password)

    def click_login_button(self):
        login_button = self.wait_for_element(self.login_button)
        login_button.click()
