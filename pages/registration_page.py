from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    ERROR_TEXT = "Input payload validation failed"
    SECONDARY_EMAIL_USE = " is already registered"
    PASSWORD = "Test_qa_2"
    email_field = (By.ID, "email")
    password_field = (By.ID, "password")
    signup_button = (By.CSS_SELECTOR, "[type='submit']")
    error = (By.XPATH, "//*[@id='form-alert']/div/div/div")
    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        self.find_element(self.email_field).send_keys(email)

    def enter_password(self, password):
        self.find_element(self.password_field).send_keys(password)

    def click_signup_button(self):
        self.find_element(self.signup_button).click()

    def signup(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_signup_button()

    def check_error_text(self):
        text = self.find_element(self.error).text
        return text
