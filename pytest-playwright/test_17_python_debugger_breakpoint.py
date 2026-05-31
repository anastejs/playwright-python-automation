# breakpoint() - встроенная функция Python для запуска интерактивного отладчика (debugger) в месте выполнения программы,
# позволяет пошагово выполнять код (что-то вроде REPL); работает в любом .py коде

from playwright.sync_api import Page, expect


# проверка - ссылка docs видима
def test_page_has_docs_link(page: Page):
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="docs")
    expect(link).to_be_visible()

# проверка - переход на нужную страницу
def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="GET STARTED")

    breakpoint()   # запускает python debugger !

    link.click()
    expect(page).to_have_url("https://playwright.dev/python/docs/intro")


#  pytest test_python_debugger_breakpoint.py