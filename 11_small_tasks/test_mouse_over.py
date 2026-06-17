# Тест проверяет поведение элемента при наведении мыши

from playwright.sync_api import Page, expect


def test_mouse_over(page: Page):
    page.goto("http://uitestingplayground.com/mouseover")
    # Наводим мышь на "Click me"
    link = page.get_by_title("Click me")
    link.hover()

    # Проверяем, что текст ссылки изменился на "Active link"
    active_link = page.get_by_title("Active link")
    
    active_link.click(click_count=2)
    click_count = page.locator("span#clickCount")
    
    expect(click_count).to_have_text("2")