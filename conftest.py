import random
import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options)
    browser.find_elements()
    yield browser
    browser.quit()

@pytest.fixture(scope="module")
def email():
    random_number_1 = str(random.randint(0, 999))
    random_number_2 = str(random.randint(0, 999))
    email = "test" + random_number_1 + random_number_2 + "@test.qa"
    return email
