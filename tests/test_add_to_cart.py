import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_add_backpack_to_cart(page):
    # 1. 登录
    login_page = LoginPage(page)
    login_page.navigate("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_login_successful(), "登录失败"

    # 2. 在商品页点击添加背包
    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()

    # 3. 验证购物车角标变成 1（表示添加成功）
    # 查找购物车图标的数字部分（SauceDemo 的购物车徽章有 class "shopping_cart_badge"）
    cart_badge = page.locator(".shopping_cart_badge")
    assert cart_badge.inner_text() == "1", "购物车数量不是1，添加失败"

    