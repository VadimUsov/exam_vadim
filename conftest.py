import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options)
    yield browser
    browser.quit()
