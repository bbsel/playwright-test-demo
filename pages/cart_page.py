from pages.base_page import BasePage

class CartPage(BasePage):
    # 结账按钮的 ID 选择器（SauceDemo 购物车页面）
    CHECKOUT_BUTTON = "#checkout"

    def proceed_to_checkout(self):
        """点击 Checkout 按钮进入结账页面"""
        self.click(self.CHECKOUT_BUTTON)