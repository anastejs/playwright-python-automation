# Современные приложения часто генерируют динамические идентификаторы элементов. 
# В этом случае ID не является надежным атрибутом для поиска элемента.
# Не использовать ID 

from playwright.sync_api import Page, expect


def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/dynamicid")
    button = page.get_by_role("button", name="Button with Dynamic ID")    # находим кнопку по её названию
    expect(button).to_be_visible()

    button.click()