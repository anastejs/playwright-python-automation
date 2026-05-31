import pytest    #для создания fixture 
from playwright.sync_api import BrowserContext, Page

DOCS_URL = "https://playwright.dev/python/docs/intro"

@pytest.fixture(autouse=True)    # автоматически использовать эту фикстуру перед каждым тестом
def trace_test(context: BrowserContext):
    # start tracing
    context.tracing.start(
        name="playwright",
        screenshots=True,
        snapshots=True,
        sources=True,
    )
    # pause until test function finishes
    yield
    # stop tracing and save it
    context.tracing.stop(path="trace.zip")


def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="GET STARTED")
    link.click()
    
    assert page.url == DOCS_URL

# Trace - это детальная интерактивная запись выполнения теста, которая позволяет пошагово увидеть всё, 
# что происходило в браузере и внутри Playwright (все действия, DOM, network и ошибки для удобного дебага).

# чтобы просмотреть trace.zip -> в терминале команда: playwright show-trace trace.zip