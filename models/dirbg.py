from playwright.sync_api import expect


class DirBgPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://dir.bg/"
        self.accept_cookies = page.locator(".fc-cta-consent")
        self.today_link = page.locator("#nav-item-3")
        self.today_url = "https://dnes.dir.bg/"

    def navigate(self):
        self.page.goto(self.url)
        # self.accept_cookies.click()

    def go_to_today(self):
        self.today_link.click()

    def assert_today_page(self):
        self.page.wait_for_load_state()
        expect(self.page).to_have_url(self.today_url)
