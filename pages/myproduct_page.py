class MyProductsPage:
    def __init__(self, page):
        self.page = page
        self.my_products_link = page.locator("a.item", has_text="My Products")
        self.delete_yes_button = page.get_by_role("button", name="Yes, delete")

    def move_to_my_products(self):
        self.my_products_link.click()

    def get_product_card(self, title: str):
        return self.page.get_by_text(title, exact=True).first

    def open_product(self, title: str):
        self.get_product_card(title).first.click()
    
    def delete_product(self, title: str):
        self.get_product_card(title).locator("xpath=../..").locator("button.ui.icon.button").click()
        self.delete_yes_button.click()