from playwright.sync_api import expect

def test_valid_register(register_page):
    register_page.open()
    register_page.moveToRegisterPage()
    register_page.register("zaman", "shekh", "Mirpur, Dhaka", "test@gmail.com", "12345", "12345", "12345")