# Test hooks — это механизмы, которые позволяют выполнять подготовительные или завершающие действия до и после запуска тестов. 
# Используются для выполнения действий до и после тестов, например открытия браузера, подготовки тестовых данных, авторизации или очистки окружения.

import pytest       #для создания fixture 
from playwright.sync_api import Page   #чтобы появилась подсказка для page

DOCS_URL = "https://playwright.dev/python/docs/intro"


# пример 2 - как использовать фикстуру немного с другим синтаксисом, с autouse=True
# зачем нужен autouse=True? - чтобы не нужно было явно указывать эту фикстуру в каждом тесте, to simplify the setup and cleanup automatically
@pytest.fixture(autouse=True, scope="function")   #автоматически использовать эту фикстуру перед каждым тестом
def visit_playwright(page: Page):
    page.goto("https://playwright.dev/python")
    yield page     #перед тестом выполняется код до yield, после теста выполняется код после yield
    page.close()
    print("\n[ FIXTURE ]: page closed!")

def test_page_has_docs_link(page: Page):      #это строка означает, что pytest сам создаст browser/context/page перед тестом и сам всё закроет после теста
    link = page.get_by_role("link", name="Docs")
    assert link.is_visible()

def test_get_started_visits_docs(page: Page):
    page.get_by_role("link", name="Get started").click()
    assert page.url == DOCS_URL


#в терминале
#pytest
#pytest --headed --slowmo=500
#pytest --headed --browser=webkit --slowmo=1000
