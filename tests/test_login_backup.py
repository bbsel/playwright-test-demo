# test_login.py 包含具体的测试用例。
# 文件名以 test_ 开头，Pytest 会自动收集其中的测试函数。

import pytest                     # 虽然当前没用到 pytest 的直接装饰器，但运行需要导入
from pages.login_page import LoginPage   # 导入上面定义的 LoginPage 类

# 测试函数：验证使用正确用户名和密码能够成功登录
# 参数 page 来自 conftest.py 中定义的 page fixture，Pytest 会自动注入
def test_valid_login(page):
    # 1. 创建 LoginPage 对象，传入 page fixture 提供的浏览器页面实例
    login_page = LoginPage(page)

    # 2. 导航到 SauceDemo 的登录页面
    login_page.navigate("https://www.saucedemo.com/")

    # 3. 执行登录操作：输入用户名 standard_user 和密码 secret_sauce
    login_page.login("standard_user", "secret_sauce")

    # 4. 断言登录是否成功：调用 is_login_successful 方法，期望返回 True
    # 如果返回 False，则抛出 AssertionError，并显示后面的错误消息
    assert login_page.is_login_successful(), "登录失败，未跳转到商品页"