from pages.base_page import BasePage

class ProductsPage(BasePage):
    # 定位器：Sauce Labs Backpack 的“添加到购物车”按钮
    BACKPACK_ADD_BUTTON = "#add-to-cart-sauce-labs-backpack"
    # 购物车图标
    SHOPPING_CART_LINK = ".shopping_cart_link"

    def add_backpack_to_cart(self):
        """将 Sauce Labs Backpack 加入购物车"""
        self.click(self.BACKPACK_ADD_BUTTON)

    def go_to_cart(self):
        """点击购物车图标进入购物车页面"""
        self.click(self.SHOPPING_CART_LINK)