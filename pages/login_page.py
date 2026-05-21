# login_page.py 针对登录页面定义专属的操作和元素定位。
# 它继承 BasePage，因此自动拥有 navigate、click、fill 等方法。

from pages.base_page import BasePage

class LoginPage(BasePage):
    # 类变量（通常大写）存储元素的定位符
    # 这样做的好处是：如果页面元素 ID 或 class 发生变化，只需修改这里一处即可
    USERNAME_INPUT = "#user-name"      # 用户名输入框的 CSS 选择器
    PASSWORD_INPUT = "#password"       # 密码输入框的 CSS 选择器
    LOGIN_BUTTON   = "#login-button"   # 登录按钮的 CSS 选择器

    # 登录动作的封装：输入用户名、密码，然后点击登录按钮
    def login(self, username: str, password: str):
        # self.fill 继承自 BasePage，在指定选择器的元素中输入文本
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)   # self.click 也继承自 BasePage

    # 判断登录是否成功的辅助方法
    # 根据登录成功后页面的 URL 特征（包含 "inventory.html"）来返回布尔值
    def is_login_successful(self) -> bool:
        # page.url 是 Playwright 提供的当前页面 URL 属性
        return "inventory.html" in self.page.url