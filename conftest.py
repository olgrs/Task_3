import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from data import BASE_URL, FEED_URL
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.profile_page import ProfilePage
from pages.feed_page import FeedPage
from helpers import create_user_via_api, delete_user_via_api


# ---------------- CLI OPTION ----------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox"
    )


# ---------------- DRIVER FIXTURE ----------------
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(5)

    yield driver
    driver.quit()


# ---------------- PAGES ----------------
@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(BASE_URL)
    return page


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)


@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver)


@pytest.fixture
def feed_page(driver):
    page = FeedPage(driver)
    page.go_to_url(FEED_URL)
    return page


# ---------------- USER FIXTURE ----------------
@pytest.fixture
def test_user():
    email, password, token = create_user_via_api()
    yield email, password, token
    delete_user_via_api(token)

@pytest.fixture
def logged_in_user(driver, main_page, login_page, test_user):
    email, password, token = test_user

    main_page.open()
    main_page.click_login_button()
    login_page.login(email, password)
    main_page.wait_for_url_to_be(BASE_URL)
    return email, password, token
