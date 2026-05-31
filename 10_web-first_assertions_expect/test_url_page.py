#Playwright Web-First Assertions — это способ проверок, где Playwright сам "ждёт" нужное состояние страницы, прежде чем выполнить assert.
#Проблема без Web-first: assert page.locator("text=Success").is_visible()   ->
#если элемент появится через 2 секунды → тест упадёт, потому что проверка была слишком ранней.

#Web-first assertion, как работает? проверяет - не видит элемент - ждёт немного - проверяет снова - повторяет до таймаута
#То есть это auto-wait для assertions. Cам повторяет проверки, устойчив к async UI

from playwright.sync_api import Page, expect

DOCS_URL = "https://playwright.dev/python/docs/intro"

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="GET STARTED")
    link.click()
    
    # assert statement -хуже для UI-тестов, проверяет состояние мгновенно и не ждёт загрузки/изменений страницы, из-за чего тесты часто становятся flaky
    # assert page.url == DOCS_URL
    # expect page url
    expect(page).to_have_url(DOCS_URL)
    # expect page title
    expect(page).to_have_title("Installation | Playwright Python")