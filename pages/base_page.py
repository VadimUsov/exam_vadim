from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver




    def find_element(self, args):
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(EC.element_to_be_clickable(self.driver.find_element(*args)))
        return element

    def find_elements(self, args):
        elements = self.driver.find_elements(*args)
        return elements

    def open_site(self):
        self.driver.get("http://127.0.0.1:8081/")
