import pytest
from playwright.sync_api import Playwright, sync_playwright
from models.dirbg import DirBgPage


def test_today(set_up):
    page = set_up
    dirbg_page = DirBgPage(page)
    dirbg_page.navigate()
    # dirbg_page.go_to_today()
    # dirbg_page.assert_today_page()


# @pytest.mark.xfail
def test_fail(set_up):
    page = set_up
    dirbg_page = DirBgPage(page)
    dirbg_page.navigate()
    # dirbg_page.go_to_today()
    # dirbg_page.assert_today_page()
    print("Success")
    # ---------------------
    # context.close()
    # browser.close()
