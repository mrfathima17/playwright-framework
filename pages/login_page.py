from utilities.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"
    ERROR_MSG = "[data-test='error']"

    def login(self, username, password):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)