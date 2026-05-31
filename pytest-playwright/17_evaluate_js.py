# evaluate() - для выполнения JavaScript-кода прямо внутри страницы браузера
# выполняет код внутри вкладки такой же, как если открыть DevTools → Console и написать там js код

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://playwright.dev/python")

    # примеры использования evaluate()
    page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
    page.screenshot(path="end_of_the_page.jpg")

    title = page.evaluate("document.title")
    print(title)

# python 17_evaluate_js.py