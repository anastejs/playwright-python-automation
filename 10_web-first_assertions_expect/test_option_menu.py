from playwright.sync_api import Page, expect


def test_app(page: Page):
    page.goto("https://bootswatch.com/default")

    option_menu = page.get_by_label("Example select")    # выбираем выпадающее меню с вариантами ответов
    # проверка - ожидаем, что в выпадающем меню выбран вариант с value="1"
    expect(option_menu).to_have_value("1")

    multi_option_menu = page.get_by_label("Example multiple select")
    multi_option_menu.select_option(["2", "4"])
    # проверка - ожидаем, что в выпадающем меню выбраны варианты с value="2" и value="4"
    expect(multi_option_menu).to_have_values(["2", "4"])