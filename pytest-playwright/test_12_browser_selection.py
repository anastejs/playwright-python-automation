# тестируем декораторы для выбора браузера: @pytest.mark.skip_browser и @pytest.mark.only_browser

import pytest       #для создания fixture 
from playwright.sync_api import Page, expect

DOCS_URL = "https://playwright.dev/python/docs/intro"


@pytest.mark.skip_browser("firefox")  # пропускаем тест для Firefox
def test_page_has_docs_link(browser_name: str, page: Page):
    # if browser_name != "firefox":       # эту строчку кода заменили на fixture выше
    page.goto("https://playwright.dev/python")
    docs_link = page.get_by_role("link", name="Docs")
    expect(docs_link).to_be_visible()

@pytest.mark.only_browser("firefox")      # запускаем тест только для Firefox
def test_get_started_visits_docs(is_firefox: bool, page: Page):    
    # if is_firefox:                       # эту строчку кода заменили на fixture выше
    page.goto("https://playwright.dev/python")
    page.get_by_role("link", name="Get started").click()
    expect(page).to_have_url(DOCS_URL)



#в терминале
#pytest
#pytest --headed --slowmo=500 --browser=firefox -v