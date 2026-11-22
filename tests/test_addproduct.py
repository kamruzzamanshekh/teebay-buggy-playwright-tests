import re
from time import time
from playwright.sync_api import expect

product_title = "New_Product"

def test_addproduct_happy_path(add_product_page):
    add_product_page.click_add_product_button()
    add_product_page.add_a_product(product_title, "khob e valo product", 123,123)


def test_add_product_negative_price_integrity(add_product_page, my_products):
    my_products.move_to_my_products()
    invalid_title = f"Negative_Price_Test_{int(time())}"

    add_product_page.click_add_product_button()
    add_product_page.add_a_product(invalid_title, "Negative price check", -123, 123)

    expect(my_products.get_product_card(invalid_title)).to_have_count(0)

def test_verify_product_in_myproduct_card(my_products):
    my_products.get_product_card(product_title)

def test_open_product(my_products):
    my_products.open_product(product_title)
