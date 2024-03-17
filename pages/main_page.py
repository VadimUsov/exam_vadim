from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    signup_button = (By.CSS_SELECTOR, "[href='/signup']")
    signin_button = (By.CSS_SELECTOR, "[href='/signin']")
    junior_config_price = (By.XPATH, "//*[@id='Price']/div[1]/div[2]/a")
    junior_config = (By.XPATH, "//*[@id='Price']/div[1]/div[2]/p")
    middle_config_price = (By.XPATH, "//*[@id='Price']/div[2]/div[2]/a")
    middle_config = (By.XPATH, "//*[@id='Price']/div[2]/div[2]/p")
    senior_config_price = (By.XPATH, "//*[@id='Price']/div[3]/div[2]/a")
    senior_config = (By.XPATH, "//*[@id='Price']/div[3]/div[2]/p")
    free_lancer_config_price = (By.XPATH, "//*[@id='Price']/div[4]/div[2]/a")
    free_lancer_config = (By.XPATH, "//*[@id='Price']/div[4]/div[2]/p")
    fan_config_price = (By.XPATH, "//*[@id='Price']/div[5]/div[2]/a")
    fan_config = (By.XPATH, "//*[@id='Price']/div[5]/div[2]/p")


    def __init__(self, driver):
        super().__init__(driver)

    def get_config_price(self, locator):
        price = (self.find_element(locator).text).split("$")
        return int(price[1])

    def calculate_config_price(self, locator):
        config = (self.find_element(locator).text).split()
        summa = int(config[0]) ** 2 + int(config[2]) * 2 + int(config[5]) / 4
        return summa

    def signup_button_click(self):
        self.find_element(self.signup_button).click()

    def signin_button_click(self):
        self.find_element(self.signin_button).click()

