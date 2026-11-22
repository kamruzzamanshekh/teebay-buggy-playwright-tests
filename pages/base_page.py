from playwright.sync_api import expect


class BasePage:
    def __init__(self, page):
        self.page = page
        self.logout_item = page.locator("a.item, button").filter(has_text="Logout").first
        self.logout_yes_button = page.get_by_role("button", name="Yes I am sure!")
        self.sigin_button = page.locator("button[type='submit']")

    def logout(self):
        self.logout_item.click()
        self.logout_yes_button.click()
        expect(self.sigin_button).to_be_visible()
