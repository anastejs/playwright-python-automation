# page.on("request", on_request) и page.on("response", on_response)

# Event listener - ждёт определённое событие и автоматически реагирует, когда событие происходит
# Network listeners — это взаимодействия между веб-браузером и сервером, такие как request или response
# Что можно получить из HTTP request? URL, method (GET), headers, payload
# Что можно получить из HTTP response? Status code, headers, payload/body, cookies, response time

from playwright.sync_api import Request, Response, Page, expect

DOCS_URL = "https://playwright.dev/python/docs/intro"


def on_request(request: Request):
    print("Sent Request:", request)

def on_response(response: Response):
    print("Got Response:", response)

def test_page_has_docs_link(page: Page):
    # Когда произойдёт request event — вызови функцию on_request
    page.on("request", on_request)
    # Когда произойдёт response event — вызови функцию on_response
    page.on("response", on_response)

    page.goto("http://playwright.dev/python")
    docs_link = page.get_by_role("link", name="Docs")
    docs_link.click()
    expect(page).to_have_url(DOCS_URL)