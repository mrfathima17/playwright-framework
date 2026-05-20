import json
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

with open("testdata/data.json") as f:
    data = json.load(f)

# ─── LOGIN TESTS ───────────────────────────────────────────

def test_valid_login(page):
    login = LoginPage(page)
    products = ProductsPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    assert products.get_title() == "Products"

def test_invalid_login(page):
    login = LoginPage(page)
    login.login(
        data["invalid_user"]["username"],
        data["invalid_user"]["password"]
    )
    assert "Epic sadface" in login.get_error_message()

def test_locked_out_user(page):
    login = LoginPage(page)
    login.login(
        data["locked_user"]["username"],
        data["locked_user"]["password"]
    )
    assert "locked out" in login.get_error_message()

# ─── PRODUCT TESTS ─────────────────────────────────────────

def test_products_page_loads(page):
    login = LoginPage(page)
    products = ProductsPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    assert products.get_title() == "Products"

def test_sort_products_low_to_high(page):
    login = LoginPage(page)
    products = ProductsPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    products.sort_products("lohi")
    prices = products.get_product_prices()
    assert prices == sorted(prices)

def test_sort_products_high_to_low(page):
    login = LoginPage(page)
    products = ProductsPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    products.sort_products("hilo")
    prices = products.get_product_prices()
    assert prices == sorted(prices, reverse=True)

# ─── CART TESTS ────────────────────────────────────────────

def test_add_product_to_cart(page):
    login = LoginPage(page)
    products = ProductsPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    products.add_first_product_to_cart()
    assert products.get_cart_count() == "1"

def test_remove_product_from_cart(page):
    login = LoginPage(page)
    products = ProductsPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    products.add_first_product_to_cart()
    products.remove_first_product_from_cart()
    assert products.get_cart_count() == "0"

# ─── CHECKOUT TESTS ────────────────────────────────────────

def test_complete_checkout(page):
    login = LoginPage(page)
    products = ProductsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )
    products.add_first_product_to_cart()
    products.go_to_cart()
    assert cart.get_title() == "Your Cart"
    cart.click_checkout()
    checkout.fill_checkout_info(
        data["checkout_info"]["first_name"],
        data["checkout_info"]["last_name"],
        data["checkout_info"]["postal_code"]
    )
    checkout.finish_order()
    assert checkout.get_complete_message() == "Thank you for your order!"