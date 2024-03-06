class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, args):
        return self.driver.find_element(*args)

    def open_site(self):
        self.driver.get("http://127.0.0.1:8081/")