import pytest
from selene import browser, Browser, Config
from selenium import webdriver
import allure
import os
from selenium.webdriver.chrome.options import Options
from utils import attach
from dotenv import dotenv_values, load_dotenv
# Без селиноида, локально:
# @pytest.fixture(scope="function")
# def open_browser():
#     # browser.config.driver_name = 'firefox'
#     # browser.config.driver_options = webdriver.FirefoxOptions()
#     browser.open('https://ostrovok.ru/')
#     yield browser
#     attach.add_html(browser)
#     attach.add_logs(browser)
#     attach.add_screenshot(browser)
#     browser.quit()

# @pytest.fixture(scope="session", autouse=True)
# def load_env():
#     load_dotenv()
@pytest.fixture(scope="function")
def open_selenoid(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    # login = os.getenv('LOGIN')
    # password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        # command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser = Browser(Config(driver))
    browser.open('https://ostrovok.ru/')
    yield browser
    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_screenshot(browser)
    # Только для селеноида:
    attach.add_video(browser)
    browser.quit()