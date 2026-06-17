# Тест проверяет, что значение текстового поля передается на кнопку после клика

from playwright.sync_api import Page, expect


def test_text_input(page: Page):
    page.goto("http://uitestingplayground.com/textinput")
    query = "great stuff"

    input = page.get_by_label("Set New Button Name")
    input.fill(query)

    btn = page.locator("button.btn-primary")
    btn.click()
    # expect button text to be input value
    expect(btn).to_have_text(query)