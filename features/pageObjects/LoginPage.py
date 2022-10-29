from features.pageObjects.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.type("username_CSS", username)

    def enter_password(self, password):
        self.type("password_CSS", password)

    def submit_login(self):
        self.click("login_XPATH")
