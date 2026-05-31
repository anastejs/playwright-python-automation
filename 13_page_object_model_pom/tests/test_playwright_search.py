# тестируе поиск на странице и вывод результатов

from pages.playwright_page import PlaywrightPage
from playwright.sync_api import Page, expect

def test_docs_link(page: Page):
    homepage = PlaywrightPage(page)
    homepage.visit_docs()
    # проверка - страница перешла на нужную ссылку
    expect(homepage.page).to_have_url("https://playwright.dev/python/docs/intro")

def test_docs_search(page: Page):
    query = "assertions"

    homepage = PlaywrightPage(page)
    homepage.search(query)

    # проверка - в результатах поиска есть нужный текст
    expect(homepage.search_results()).to_contain_text("List of assertions")