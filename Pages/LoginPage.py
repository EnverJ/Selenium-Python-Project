from selenium import webdriver
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage

"""By Locators"""


class LoginPage(BasePage):
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    """constructor of the class"""

    def __init__(self, driver):
        super().__init__(driver)

        self.driver.get(TestData.BASE_URL)

    """"Page Actions"""

    """this is used to get the page title"""

    def get_login_title(self, title):
        return self.get_tittle(title)

    """this is used to check sighup link"""

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    """this is used to login to the page"""

    def do_login(self, username, password):
        self.do_send_key(self, username)
        self.do_send_key(self, password)
        self.do_click(self.LOGIN_BUTTON)
