import re
from playwright.sync_api import expect


def test_valid_login(base_page):
    base_page.logout() 
    