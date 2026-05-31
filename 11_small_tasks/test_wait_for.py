# Тест должен иметь возможность дождаться появления элемента.
from playwright.sync_api import Page, expect


def test_load_delay(page: Page):
    page.goto("http://www.uitestingplayground.com/ajax")

    page.get_by_role("button", name="Button Triggering AJAX Request").click()

    paragraph = page.locator("p.bg-success")
    paragraph.click()
    # ждем 15 секунд (по условию задания), пока элемент загрузится и станет видимым
    paragraph.wait_for()
    # проверка - элемент видим
    expect(paragraph).to_be_visible()