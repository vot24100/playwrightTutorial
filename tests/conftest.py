import pytest
from playwright.sync_api import Playwright


# @pytest.fixture
# def set_up(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     context = browser.new_context()
#     page = context.new_page()
#
#     yield page

@pytest.fixture()
def set_up(page):
    yield page


# @pytest.fixture(scope='session')
# def set_up(browser):
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
