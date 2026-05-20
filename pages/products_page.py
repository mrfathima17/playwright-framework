from utilities.base_page import BasePage

class ProductsPage(BasePage):
    PAGE_TITLE = ".title"
    SORT_DROPDOWN = ".product_sort_container"
    PRODUCT_NAMES = ".inventory_item_name"
    PRODUCT_PRICES = ".inventory_item_price"
    ADD_TO_CART_BTN = "button[id^='add-to-cart']"
    REMOVE_BTN = "button[id^='remove']"
    CART_ICON = ".shopping_cart_link"
    CART_BADGE = ".shopping_cart_badge"

    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def sort_products(self, option):
        self.page.select_option(self.SORT_DROPDOWN, option)

    def get_product_names(self):
        return self.page.locator(self.PRODUCT_NAMES).all_text_contents()

    def get_product_prices(self):
        prices = self.page.locator(self.PRODUCT_PRICES).all_text_contents()
        return [float(p.replace("$", "")) for p in prices]

    def add_first_product_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BTN).first.click()

    def remove_first_product_from_cart(self):
        self.page.locator(self.REMOVE_BTN).first.click()

    def get_cart_count(self):
        if self.is_visible(self.CART_BADGE):
            return self.get_text(self.CART_BADGE)
        return "0"

    def go_to_cart(self):
        self.click(self.CART_ICON)