import time

import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.add_product_page import AddProductPage
from pages.myproduct_page import MyProductsPage
from pages.browse_products_for_rent import BrowseProductsPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def register_page(page):
    return RegisterPage(page)

@pytest.fixture
def add_product_page(page):
    return AddProductPage(page)

@pytest.fixture
def my_products(page):
    return MyProductsPage(page)

@pytest.fixture
def browse_products(page):
    return BrowseProductsPage(page)

@pytest.fixture
def base_page(page):
    return BasePage(page)

@pytest.fixture(scope="session")
def page(browser, browser_context_args):
    context = browser.new_context(**browser_context_args, no_viewport=True)
    page = context.new_page()
    yield page
    time.sleep(10)
    context.close()


@pytest.fixture(scope="session")
def browser_type_launch_args(pytestconfig, request):
    launch_options = {"args": ["--start-maximized"]}
    if pytestconfig.getoption("--headed"):
        launch_options["headless"] = False # type: ignore

    channel = pytestconfig.getoption("--browser-channel")
    if channel:
        launch_options["channel"] = channel

    slow_mo = pytestconfig.getoption("--slowmo")
    if slow_mo:
        launch_options["slow_mo"] = slow_mo

    if hasattr(request, "param"):
        launch_options.update(request.param)

    return launch_options

def pytest_collection_modifyitems(items):
    file_order = [
        "test_login.py",
        "test_addproduct.py",
        "test_update_product.py",
        "test_myproduct.py",
        "test_browse_product_for_rent.py",
        "test_logout.py",
        "test_register.py",
        
    ]

    def get_file_rank(item):
        filename = item.path.name
        return file_order.index(filename) if filename in file_order else len(file_order)

    items.sort(key=get_file_rank)