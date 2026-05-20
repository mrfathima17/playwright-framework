from utilities.base_page import BasePage

class ProductsPage(BasePage):
    PAGE_TITLE = ".title"

    def get_title(self):
        return self.get_text(self.PAGE_TITLE)