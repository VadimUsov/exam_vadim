import time
import pytest
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.signin_page import SigninPage
from pages.profile_page import ProfilePage


@pytest.mark.parametrize("price_locator, config_locator", [
    (MainPage.junior_config_price, MainPage.junior_config),
    (MainPage.middle_config_price, MainPage.middle_config),
    (MainPage.senior_config_price, MainPage.senior_config),
    (MainPage.free_lancer_config_price, MainPage.free_lancer_config),
    (MainPage.fan_config_price, MainPage.fan_config)
])
def test_correct_sum_of_config(driver, price_locator, config_locator):
    page = MainPage(driver)
    page.open_site()
    assert page.calculate_config_price(config_locator) == page.get_config_price(price_locator)


def test_successful_registration_user(driver, email):
    main_page = MainPage(driver)
    main_page.open_site()
    main_page.signup_button_click()
    page = RegistrationPage(driver)
    page.signup(email, page.PASSWORD)
    time.sleep(1)
    assert driver.current_url == "http://127.0.0.1:8081/profile"


def test_forbidden_registration_with_same_email(driver, email):
    main_page = MainPage(driver)
    main_page.open_site()
    main_page.signup_button_click()
    page = RegistrationPage(driver)
    page.signup(email, page.PASSWORD)
    time.sleep(1)
    assert page.check_error_text() == email + page.SECONDARY_EMAIL_USE


def test_forbidden_registration_with_empty_password(driver, email):
    main_page = MainPage(driver)
    main_page.open_site()
    main_page.signup_button_click()
    page = RegistrationPage(driver)
    page.signup(email, "")
    time.sleep(5)
    assert driver.current_url == "http://127.0.0.1:8081/signup"


def test_forbidden_registration_with_incorrect_email(driver):
    main_page = MainPage(driver)
    main_page.open_site()
    main_page.signup_button_click()
    page = RegistrationPage(driver)
    page.signup(page.PASSWORD, page.PASSWORD)
    time.sleep(1)
    assert page.ERROR_TEXT == page.check_error_text()


def test_successful_authorization(driver, email):
    main_page = MainPage(driver)
    main_page.open_site()
    main_page.signin_button_click()
    page = SigninPage(driver)
    page.signin(email, page.PASSWORD)
    time.sleep(2)
    assert driver.current_url == "http://127.0.0.1:8081/profile"


def test_forbidden_authorization_with_incorrect_creds(driver, email):
    main_page = MainPage(driver)
    main_page.open_site()
    main_page.signin_button_click()
    page = SigninPage(driver)
    page.signin(email, page.INCORRECT_PASSWORD)
    time.sleep(1)
    assert page.ERROR_TEXT == page.check_error()


def test_cookies_changes(driver, email):
    main_page = MainPage(driver)
    main_page.open_site()
    main_page.signin_button_click()
    page = SigninPage(driver)
    time.sleep(1)
    cookies = page.get_cookies()
    page.signin(email, page.PASSWORD)
    time.sleep(1)
    assert cookies != page.get_cookies()


def test_create_three_servers(driver, email):
    main_page = MainPage(driver)
    main_page.open_site()
    main_page.signin_button_click()
    page = SigninPage(driver)
    page.signin(email, page.PASSWORD)
    time.sleep(1)
    profile_page = ProfilePage(driver)
    profile_page.order_servers(3, profile_page.CPU, profile_page.DOMAIN)
    time.sleep(1)
    servers = profile_page.number_of_servers()
    assert 3 == len(servers)


def test_deletion_server(driver, email):
    main_page = MainPage(driver)
    main_page.open_site()
    main_page.signin_button_click()
    page = SigninPage(driver)
    page.signin(email, page.PASSWORD)
    time.sleep(2)
    profile_page = ProfilePage(driver)
    start_number_of_servers = len(profile_page.number_of_servers())
    profile_page.delete_server()
    profile_page.confrim_deletion()
    time.sleep(2)
    current_number_of_servers = len(profile_page.number_of_servers())
    assert start_number_of_servers - 1 == current_number_of_servers


def test_cpu_is_text(driver, email):
    main_page = MainPage(driver)
    main_page.open_site()
    main_page.signin_button_click()
    page = SigninPage(driver)
    page.signin(email, page.PASSWORD)
    time.sleep(1)
    profile_page = ProfilePage(driver)
    profile_page.order_servers(1, "XEON", profile_page.DOMAIN)
    assert profile_page.ERROR_TEXT == profile_page.check_error_text()


def test_incorrect_domain(driver, email):
    main_page = MainPage(driver)
    main_page.open_site()
    main_page.signin_button_click()
    page = SigninPage(driver)
    page.signin(email, page.PASSWORD)
    time.sleep(1)
    profile_page = ProfilePage(driver)
    profile_page.order_servers(1, profile_page.CPU, "domain")
    time.sleep(1)
    assert profile_page.ERROR_TEXT == profile_page.check_error_text()
