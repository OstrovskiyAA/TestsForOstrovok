import pytest
from selene import browser
from selenium import webdriver
import allure
import os
from selenium.webdriver.chrome.options import Options
from utils import attach

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

@pytest.fixture(scope="function")
def open_selenoid(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100",
        "selenoid:options": {
            "enableVideo": True,
            "enableVNC": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver
    browser.open('https://ostrovok.ru/')
    yield browser
    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_screenshot(browser)
    # Только для селеноида:
    attach.add_video(browser)
    browser.quit()