class LoginPage:
    def __init__(self, page):
        self.page = page
        self.useremail = page.locator("input[name='email']")
        self.password = page.locator("input[name='password']")
        self.signIn_btn = page.locator("button[type='submit']")

    def open(self):
        self.page.goto("https://ehsanur-rahman-sazim.github.io/teebay-buggy/")

    def login(self, user, pwd):
        self.useremail.fill(user)
        self.password.fill(pwd)
        self.signIn_btn.click()