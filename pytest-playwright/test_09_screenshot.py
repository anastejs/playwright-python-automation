from playwright.sync_api import Page   #чтобы появилась подсказка для page

DOCS_URL = "https://playwright.dev/python/docs/intro"

def test_get_started_visits_docs(page: Page):
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="Get started")

    link.screenshot(path="get_started_link.png")   #сделать скриншот элемента
    link.click()
   
    page.screenshot(path="docs.png")   #сделать скриншот
    page.screenshot(path="full_docs.png", full_page=True)   #сделать скриншот всей страницы

    assert page.url == DOCS_URL