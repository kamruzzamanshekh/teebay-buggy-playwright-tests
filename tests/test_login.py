import os
import re

import pytest
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

def test_valid_login(login_page):
    email = os.getenv("TEST_USER_EMAIL")
    password = os.getenv("TEST_USER_PASSWORD")
    if not email or not password:
        pytest.fail("Set TEST_USER_EMAIL and TEST_USER_PASSWORD in the project .env file.")

    login_page.open()
    login_page.login(email, password)
    expect(login_page.page).to_have_url(re.compile(r".*/my-products/?"))
    expect(login_page.page.locator("a.item", has_text="Logout")).to_be_visible()

