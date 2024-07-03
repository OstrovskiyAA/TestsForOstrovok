import pytest
from selene import browser
from selenium import webdriver
import allure

from utils import attach


@pytest.fixture(scope="function")
def open_browser():
    # browser.config.driver_name = 'firefox'
    # browser.config.driver_options = webdriver.FirefoxOptions()
    browser.open('https://ostrovok.ru/')
    yield browser
    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_screenshot(browser)
    # Только для селеноида:
    # attach.add_video(browser)
    browser.quit()