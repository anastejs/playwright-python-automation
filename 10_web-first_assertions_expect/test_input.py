from playwright.sync_api import Page, expect


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    input = page.get_by_placeholder("Search docs")   #сначала это окно (поиска) скрыто

    # проверка - input окно должно быть скрыто
    expect(input).to_be_hidden()

    # кликаем на кнопку, которая открывает окно поиска
    search_btn = page.get_by_role("button", name="Search")
    search_btn.press("Control+KeyK") 

    # проверка - input окно должно быть видимым и редактируемым (можно ввести текст)
    expect(input).to_be_editable()
    # проверка - input окно должно быть пустым
    expect(input).to_be_empty()

    # вводим текст в input окно поиска
    query = "assertions"
    input.fill(query)

    # проверка - input окно поиска должно содержать введенный текст
    expect(input).to_have_value(query)