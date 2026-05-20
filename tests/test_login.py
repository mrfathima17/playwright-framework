import json
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

with open("testdata/data.json") as f:
    data = json.load(f)

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