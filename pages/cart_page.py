from utilities.base_page import BasePage

class CartPage(BasePage):
    PAGE_TITLE = ".title"
    CART_ITEMS = ".cart_item"
    CHECKOUT_BTN = "#checkout"
    CONTINUE_SHOPPING_BTN = "#continue-shopping"

    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_cart_item_count(self):
        return self.page.locator(self.CART_ITEMS).count()

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)