# Teebay Playwright UI Tests

Python, Pytest, and Playwright test automation for the Teebay web application:
<https://ehsanur-rahman-sazim.github.io/teebay-buggy/>.

The tests use the Page Object Model (POM): page locators and actions live in
`pages/`, fixtures live in `conftest.py`, and scenarios live in `tests/`.

## Scenarios covered

- **Login:** reads credentials from `.env`, signs in, and verifies the My Products
  page and Logout link.
- **Products:** adds a product, checks that a negative purchase price is rejected,
  verifies a product in My Products, and opens it.
- **Update-related flow:** submits the `Update_title` product data and checks its
  presence in My Products; it does not currently verify editing an existing product.
- **Product deletion:** opens the confirmation dialog and confirms deletion; the
  test does not assert that the product is gone afterward.
- **Browse and rent:** searches by title and category, opens a product, books a rent
  period, and checks that rent history changes.
- **Logout:** confirms logout and verifies that the sign-in form is visible.
- **Registration:** fills and submits the registration form. The current test does
  not assert that account creation succeeded.

Some product tests share the same page and depend on the ordering configured in
`conftest.py`. Run the full suite when testing flows that depend on earlier login,
product creation, or product update steps.

## Requirements

- Python
- Microsoft Edge installed (recommended for the commands below)

The Playwright pytest plugin can also use its bundled Chromium, if it is installed
and allowed by your machine's policies.

## Setup on Windows

From the project root:

1. Create and activate a virtual environment:

   ```cmd
   py -m venv venv
   venv\Scripts\activate
   ```

2. Install project dependencies:

   ```cmd
   python -m pip install -r requirements.txt
   ```

3. Create `.env` from the example and replace the placeholders with valid Teebay
   test-account credentials:

   ```cmd
   copy .env.example .env
   ```

   The login test expects `TEST_USER_EMAIL` and `TEST_USER_PASSWORD`. Keep the real
   values private. `.env` is ignored by Git; do not commit it.

## Running tests

Run the complete suite in a visible Microsoft Edge window:

```cmd
python -m pytest --browser-channel=msedge --headed
```

Run headless:

```cmd
python -m pytest --browser-channel=msedge
```

Run one test file:

```cmd
python -m pytest tests\test_addproduct.py --browser-channel=msedge --headed
```

Run the login test:

```cmd
python -m pytest tests\test_login.py::test_valid_login --browser-channel=msedge --headed
```

The browser is configured to open maximized. The shared page stays open for the
test session, and `conftest.py` waits 10 seconds before closing its browser context.

## Project layout

```text
conftest.py                 Shared Pytest fixtures and browser setup
pytest.ini                  Test discovery and default options
requirements.txt            Python dependencies
.env.example                Credential variable names (no real secrets)
pages/                      Page Object Model classes
tests/                      Pytest test scenarios
```
