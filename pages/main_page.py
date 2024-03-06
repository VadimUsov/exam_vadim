from selenium.webdriver.common.by import By
from pages.base_page import BasePage

signup_button = (By.CSS_SELECTOR, "[href='/signup']")


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_site(self):
        self.driver.get("http://127.0.0.1:8081/")

    def signup_button(self):
        return self.find_element(signup_button)

    def signup_button_click(self):
        self.signup_button().click()