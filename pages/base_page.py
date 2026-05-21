# base_page.py 封装了所有页面都会用到的通用操作，
# 例如打开 URL、点击元素、输入文本、获取标题等。
# 其他页面类（如 LoginPage）会继承这个基类，从而复用这些方法。

class BasePage:
    # 构造函数，接收一个 Playwright 的 page 对象
    def __init__(self, page):
        self.page = page          # 将 page 保存为实例属性，供其他方法使用

    # 导航到指定 URL
    def navigate(self, url: str):
        self.page.goto(url)       # Playwright 的 goto 方法会等待页面加载完成

    # 点击页面上的元素（通过 CSS 选择器或 XPath）
    def click(self, selector: str):
        self.page.click(selector)

    # 在输入框中填充文本（会先清空再输入）
    def fill(self, selector: str, text: str):
        self.page.fill(selector, text)

    # 获取当前页面的标题
    def get_title(self) -> str:
        return self.page.title()