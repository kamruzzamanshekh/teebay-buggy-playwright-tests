class AddProductPage:
    import random
    from playwright.sync_api import expect

    def __init__(self, page):
        self.page = page
        self.add_product_btn = page.get_by_role("button", name="Add Product")
        self.title = page.locator("[name='title']")
        self.categories_dropdown = page.locator("div[role='listbox'][name='categories']")
        self.categories_option = self.categories_dropdown.locator("div[role='option']")
        self.description = page.locator("textarea[name='description']")
        self.purchase_price = page.locator("[name='purchase_price']")
        self.rent_price = page.locator("[name='rent_price']")
        self.frequency = page.locator("div[role='listbox'][name='rent_duration_type']")
        self.dropdown_option = self.frequency.locator("div[role='option']")
        self.add_button = page.locator("button[type='submit']")

    def open(self):
        self.page.goto("https://ehsanur-rahman-sazim.github.io/teebay-buggy/")

    def click_add_product_button(self):
        self.add_product_btn.click()

    def select_random_category(self): 
        self.categories_dropdown.click()
        self.expect(self.categories_option.first).to_be_visible()
        option_count = self.categories_option.count()
        if option_count == 0:
            raise RuntimeError("No category options are available")

        option = self.categories_option.nth(self.random.randrange(option_count))
        category = option.inner_text().strip()
        option.click()
        return category
    
    def select_random_duration(self): 
            self.frequency.click()
            self.expect(self.dropdown_option.first).to_be_visible()
            option_count = self.dropdown_option.count()
            if option_count == 0:
                raise RuntimeError("No category options are available")
    
            option = self.dropdown_option.nth(self.random.randrange(option_count))
            duration = option.inner_text().strip()
            option.click()
            return duration

    def add_a_product(self, title, description, purchase_price, rent_price):
        self.title.fill(title)
        self.select_random_category()
        self.description.fill(description)
        self.purchase_price.fill(str(purchase_price))
        self.rent_price.fill(str(rent_price))
        self.select_random_duration()
        self.add_button.click()
    
