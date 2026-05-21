import pytest
from playwright.sync_api import Page

def test_bilibili_search(page: Page):
    page.goto("https://www.bilibili.com/")
    page.fill(".nav-search-input", "Playwright")
    page.press(".nav-search-input", "Enter")
    # 等待标题包含关键词（最稳定的判断方式）
    page.wait_for_function("document.title.includes('Playwright')", timeout=15000)
    assert "Playwright" in page.title()