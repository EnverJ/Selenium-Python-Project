from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""This calss is the parent of all pages"""
"""it contains all the generic methids and utilities for all the pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def do_send_key(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_tittle(self, title):
        WebDriverWait(self, 10).until(EC.title_is(title))
        return self.driver.title
