import pytest
from pages.login_page import LoginPage

# 测试数据列表：每个元素是一个元组 (用户名, 密码, 期望是否登录成功)
login_test_data = [
    ("standard_user", "secret_sauce", True),      # 正确凭据
    ("locked_out_user", "secret_sauce", False),   # 锁定用户
    ("", "secret_sauce", False),                  # 空用户名
    ("standard_user", "", False),                 # 空密码
    ("problem_user", "secret_sauce", True),       # 问题用户（仍能登录）
    ("performance_glitch_user", "secret_sauce", True), # 性能故障用户
    ("invalid_user", "wrong_pass", False),        # 完全错误
]

@pytest.mark.parametrize("username,password,expected_success", login_test_data)
def test_login_scenarios(page, username, password, expected_success):
    login_page = LoginPage(page)
    login_page.navigate("https://www.saucedemo.com/")
    login_page.login(username, password)

    if expected_success:
        assert login_page.is_login_successful(), f"期望登录成功，但实际失败（用户名：{username}）"
        # 可选：登录成功后登出，以便下一个用例从头开始（因为每个用例都会新建 page，所以不需要）
    else:
        assert not login_page.is_login_successful(), f"期望登录失败，但实际成功（用户名：{username}）"