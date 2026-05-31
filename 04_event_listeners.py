# page.on(), page.once()
# page.waitForSelector(selector, state='visible') и ли просто page.waitForSelector(selector)
# state: 'attached' (элемент прикреплен к DOM), state: 'detached' (элемент откреплен от DOM), state: 'hidden' (элемент скрыт), state: 'visible' (элемент видим)
# например page.locator("a#dropdown_link1").click()

from playwright.sync_api import sync_playwright

def on_load(page):
    print("Page loaded:", page)

def on_request(request):
    print("Request sent:", page)

def on_filechooser(file_chooser):
    print("File chooser opened")
    file_chooser.set_files("01_app.py")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # слушатель событий для событий навигации

    #1. регистрируем listener
    #listener должен находится ДО действия goto()
    page.on("load", on_load)
    # page.on("domcontentloaded", on_load)
    # page.on("close", on_load)
    # page.on("response", on_load)
    page.on("request", on_request)
    page.on("filechooser", on_filechooser)

    #если хотим прослушать событие только 1 раз, сам завершит его
    #page.once("load", on_load)

    #2. listen to the event
    page.goto("https://bootswatch.com/default")

    #вставить файл
    file_input = page.get_by_label("Default file input example")
    file_input.click()

    #3. remove the listener
    page.remove_listener("load", on_load)

    browser.close()