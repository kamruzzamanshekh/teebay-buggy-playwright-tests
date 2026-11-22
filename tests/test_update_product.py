import re
from playwright.sync_api import expect

product_title = "Update_title"

def test_aupdate_product(add_product_page):
    add_product_page.add_a_product(product_title, "khob e valo product updated", 1230,123)

def test_verify_product_in_myproduct_card(my_products):
    my_products.get_product_card(product_title)
