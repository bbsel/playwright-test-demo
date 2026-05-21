# conftest.py 是 Pytest 的特殊文件，它可以被 Pytest 自动识别，
# 用于定义全局的夹具（fixture）、钩子函数或插件配置。
# 该文件中的 fixture 可以被同目录下所有测试文件共享。
import os
import pytest
from playwright.sync_api import sync_playwright

# 定义一个会话级别（session scope）的 fixture，名为 browser
# scope="session" 意味着整个测试会话（即一次 pytest 运行）只执行一次这个 fixture。
# 返回的 browser 对象会被所有测试函数复用，节省资源。
@pytest.fixture(scope="session")
def browser():
    # 使用同步 API 启动 Playwright
    # with 语句确保退出时自动调用 p.stop()
    with sync_playwright() as p:
        if os.gentenv("CI"):
           browser = p.chromium.launch(channel="chrome", headless=True)
                                                    #githubact 用无头模式
        else:
           browser = p.chromium.launch(channel="chrome", headless=False, slow_mo=1000)
                                                    #本地用有头模式，慢动作
        
        yield browser
        # 关闭浏览器，释放资源
        browser.close()

# 定义一个函数级别的 fixture，名为 page
# 默认 scope 是 "function"，即每个测试函数都会获得一个全新的 page 对象
@pytest.fixture
def page(browser):
    # 从 browser 对象创建一个新的浏览器上下文（context）
    # 上下文类似于一个独立的隐身会话，不同上下文之间的 cookies、缓存、存储都是隔离的
    context = browser.new_context()
    # 在上下文中创建一个新的页面（tab）
    page = context.new_page()
    # 将 page 对象提供给测试函数
    yield page
    # 测试函数执行完毕后，关闭上下文，从而关闭该页面及其相关资源
    context.close()

#钩子函数

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """pytest 钩子：测试失败时自动截图"""
    outcome = yield
    report = outcome.get_result()
    # 仅在测试调用失败时（不是 setup/teardown 失败）截图
    if report.when == "call" and report.failed:
        # 获取测试中的 page fixture（如果测试函数使用了 page 参数）
        page = item.funcargs.get("page", None)
        if page:
            import os
            import time
            # 创建 screenshots 目录（如果不存在）
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            # 生成截图文件名：测试名_时间戳.png
            timestamp = str(int(time.time()))
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}_{timestamp}.png")
            page.screenshot(path=screenshot_path)
            print(f"\n测试失败，截图已保存至: {screenshot_path}")