# Тест проверяет прокрутку страницы до кнопки, которая изначально не видна в области просмотра.

from playwright.sync_api import Page


def test_scrollbars(page: Page):
    page.goto("http://uitestingplayground.com/scrollbars")

    btn = page.get_by_role("button", name="Hiding Button")

    btn.scroll_into_view_if_needed()
    # click() также работает (прокручивает страницу, если кнопка не видна)
    # btn.click()

    page.screenshot(path="test-scrollbars.jpg")