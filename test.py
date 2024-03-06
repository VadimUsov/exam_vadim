import time

from pages.main_page import MainPage


def test_button(driver):
    page = MainPage(driver)
    page.open_site()
    time.sleep(3)
