from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SigninPage(BasePage):
    ERROR_TEXT = "email or password does not match"
    PASSWORD = "Test_qa_2"
    INCORRECT_PASSWORD = "INCORRECT_PASSWORD"
    email_field = (By.ID, "email")
    password_field = (By.ID, "password")
    signin_button = (By.CSS_SELECTOR, "[type='submit']")
    error = (By.XPATH, "//*[@id='form-alert']/div/div/div")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        self.find_element(self.email_field).send_keys(email)

    def enter_password(self, password):
        self.find_element(self.password_field).send_keys(password)

    def click_signin_button(self):
        self.find_element(self.signin_button).click()

    def signin(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_signin_button()

    def check_error(self):
        text = self.find_element(self.error).text
        return text

    def get_cookies(self):
        cookies = self.driver.get_cookies()
        return cookies

