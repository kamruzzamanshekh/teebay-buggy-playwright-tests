class RegisterPage:
    def __init__(self, page):
        self.page = page
        self.sigup_link = page.locator("a[href='/register']")
        self.first_name_input = page.locator("[name='firstName']")
        self.last_name_input = page.locator("[name='lastName']")
        self.address_input = page.locator("[name='address']")
        self.email_input = page.locator("[name='email']")
        self.phone_input = page.locator("[name='phoneNumber']")
        self.password_input = page.locator("[name='password']")
        self.confirm_password_input = page.locator("[name='confirmPassword']")
        self.register_button = page.locator("button[type='submit']")

    def open(self):
        self.page.goto("https://ehsanur-rahman-sazim.github.io/teebay-buggy/")

    def moveToRegisterPage(self):
        self.sigup_link.click()

    def register(self, first_name, last_name, address, email, phone, password, confirm_password):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.address_input.fill(address)
        self.email_input.fill(email)
        self.phone_input.fill(phone)
        self.password_input.fill(password)
        self.confirm_password_input.fill(confirm_password)
        self.register_button.click()