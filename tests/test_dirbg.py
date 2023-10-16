from playwright.sync_api import Playwright, sync_playwright, expect


def test_dirbg(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dir.bg/")
    # page.get_by_label("Да, към сайта", exact=True).click(timeout=10000)
    # # page.pause()
    # page.locator("#nav-item-3").get_by_role("link", name="Днес").click()
    # page.wait_for_load_state()
    # expect(page).to_have_url("https://dnes.dir.bg/")
    print("Success")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_dirbg(playwright)
