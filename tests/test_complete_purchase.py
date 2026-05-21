import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_purchase(page):
    # 1. 登录
    login_page = LoginPage(page)
    login_page.navigate("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_login_successful(), "登录失败"

    # 2. 添加商品到购物车
    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()

    # 3. 进入购物车并点击 Checkout
    products_page.go_to_cart()
    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    # 4. 填写收货信息并继续
    checkout_page = CheckoutPage(page)
    checkout_page.fill_customer_info("John", "Doe", "12345")
    checkout_page.continue_checkout()

    # 5. 完成购买
    checkout_page.finish_checkout()

    # 6. 验证成功消息
    success_msg = checkout_page.get_success_message()
    assert "Thank you for your order" in success_msg, "购买失败，未显示感谢信息"