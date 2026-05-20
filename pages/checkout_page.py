from utilities.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BTN = "#continue"
    FINISH_BTN = "#finish"
    COMPLETE_HEADER = ".complete-header"

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BTN)

    def finish_order(self):
        self.click(self.FINISH_BTN)

    def get_complete_message(self):
        return self.get_text(self.COMPLETE_HEADER)