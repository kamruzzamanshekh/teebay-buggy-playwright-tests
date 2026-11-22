import re
from playwright.sync_api import expect


class BrowseProductsPage:

    def __init__(self, page):
        self.page = page
        self.browse_products_link = page.locator("a.item", has_text="Browse Products")
        self.title_input = page.locator("[name='title']")
        self.dropdown = page.locator("div[role='listbox'][name='category']")
        self.option = self.dropdown.locator("div[role='option']")
        self.filter_btn = page.locator("button[type='submit']")
        self.rent_btn = page.get_by_role("button", name="Rent", exact=True)
        self.rent_start_date_input = page.locator("input[name='start_date']")
        self.rent_end_date_input = page.locator("input[name='end_date']")
        self.book_rent_btn = page.get_by_role("button", name="Book rent", exact=True)
        self.rent_history_div = page.locator("div").filter(has_text="Rent history:").last

    def select_category(self, category_name: str):
        self.dropdown.click()
        category_option = self.option.filter(
            has_text=re.compile(rf"^{re.escape(category_name)}$")
        )
        expect(category_option.first).to_be_visible()
        category_option.first.click()

    def filter_products(self, title: str = "", category_name: str = ""):
        self.browse_products_link.click()
        if title:
            self.title_input.fill(title)
        self.select_category(category_name)
        self.filter_btn.click()

    def get_product_card(self, title: str):
        return self.page.get_by_text(title, exact=True).first

    def click_product_for_rent(self, title: str):
        product_card = self.get_product_card(title)
        product_card.click()
        self.rent_btn.click()

    def book_rent(self, start_date: str, end_date: str):
        self.rent_start_date_input.fill(start_date)
        self.rent_end_date_input.fill(end_date)
        self.book_rent_btn.click()

    def get_rent_history_text(self) -> str:
        self.rent_history_div.wait_for(state="visible")
        return self.rent_history_div.inner_text().strip()