from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # 定位器
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    COMPLETE_HEADER = ".complete-header"

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str):
        """填写收货信息"""
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.POSTAL_CODE_INPUT, postal_code)

    def continue_checkout(self):
        """点击 Continue 按钮"""
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        """点击 Finish 按钮完成购买"""
        self.click(self.FINISH_BUTTON)

    def get_success_message(self) -> str:
        """获取成功完成购买的提示文本"""
        return self.page.text_content(self.COMPLETE_HEADER)