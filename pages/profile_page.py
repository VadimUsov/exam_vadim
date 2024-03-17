from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProfilePage(BasePage):
    CPU = 1
    DOMAIN = "http://test.com"
    ERROR_TEXT = "Input payload validation failed"
    order_server_button = (By.CSS_SELECTOR, ".btn-primary[type='button']")
    domain = (By.ID, "info_url")
    cpu = (By.ID, "cpu")
    order_button = (By.CSS_SELECTOR, ".btn-primary[type='submit']")
    servers_list = (By.XPATH, "//*[@id='server-list']/div")
    delete_server_button = (By.CSS_SELECTOR, ".del-server-btn")
    error = (By.CSS_SELECTOR, ".alert-dismissible")
    def __init__(self, driver):
        super().__init__(driver)

    def click_order_server_button(self):
        self.find_element(self.order_server_button).click()

    def enter_cpu(self, cpu):
        self.find_element(self.cpu).clear()
        self.find_element(self.cpu).send_keys(cpu)

    def enter_domain(self, domain):
        self.find_element(self.domain).clear()
        self.find_element(self.domain).send_keys(domain)

    def click_order_button(self):
        self.find_element(self.order_button).click()

    def order_servers(self, number_of_servers, cpu, domain):
        for i in range(number_of_servers):
            self.click_order_server_button()
            self.enter_cpu(cpu)
            self.enter_domain(domain)
            self.click_order_button()
            self.CPU += 1

    def number_of_servers(self):
        servers = self.find_elements(self.servers_list)
        return servers

    def delete_server(self):
        self.find_element(self.delete_server_button).click()

    def confrim_deletion(self):
        self.driver.switch_to.alert.accept()

    def check_error_text(self):
        text = self.find_element(self.error).text
        return text



