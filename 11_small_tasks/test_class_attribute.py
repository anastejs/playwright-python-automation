#Нужно правильно прописать класс для кнопки
from playwright.sync_api import Page, expect


def test_class_attribute(page: Page):
    page.goto("http://uitestingplayground.com/classattr")

    # locator - css selector
    primary_btn = page.locator("button.btn-primary")

    # locator - xpath
    primary_btn = page.locator("//button[ contains(@class, 'btn-primary') ]")

    expect(primary_btn).to_be_visible()
    primary_btn.click()