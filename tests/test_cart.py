import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_proceed_to_checkout(page):
    # 1. 登录
    login_page = LoginPage(page)
    login_page.navigate("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_login_successful(), "登录失败"

    # 2. 添加一个商品到购物车（确保购物车非空）
    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()

    # 3. 进入购物车
    products_page.go_to_cart()

    # 4. 点击 Checkout
    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    # 5. 验证进入了结账信息填写页面（URL 包含 checkout-step-one.html）
    assert "checkout-step-one.html" in page.url, "未能进入结账页面"