from playwright.sync_api import expect


def test_search_product(browse_products):
    browse_products.filter_products(title="Lawn Mower", category_name="Outdoor")
    product_card = browse_products.get_product_card("Lawn Mower")
    expect(product_card).to_be_visible()

def test_click_product_for_rent(browse_products):
    browse_products.click_product_for_rent("Lawn Mower")
    prev_history_text = browse_products.get_rent_history_text()
    browse_products.book_rent(start_date="2024-06-01", end_date="2024-07-10")
    post_history_text = browse_products.get_rent_history_text()
    assert prev_history_text != post_history_text