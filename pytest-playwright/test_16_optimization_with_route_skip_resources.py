import pytest
from playwright.sync_api import Page, expect, Route

# способ отключить js scripts для всех тестов
@pytest.fixture
def browser_context_args():
    return {
        "java_script_enabled": False
    }


NOT_ALLOWED_RESOURCES = ("image", "font", "stylesheet", "media")  #список блокируемых ресурсов


def on_route(route: Route):
    # если запрос относится к блокируемым - блокирум его
    if route.request.resource_type in NOT_ALLOWED_RESOURCES:
        route.abort()
    else:
        route.continue_()


@pytest.fixture(autouse=True)     # автоматически для всех тестов
def skip_resources(page: Page):
    page.route("**", on_route)    # перехватываем все запросы


# проверка - ссылка docs видима
def test_page_has_docs_link(page: Page):
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="docs")
    expect(link).to_be_visible()

# проверка - переход на нужную страницу
def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="GET STARTED")
    link.click()
    expect(page).to_have_url("https://playwright.dev/python/docs/intro")

# для 1-2 тестов время может не сильно сократиться, но для большего объема тестов - оптимизация будет значительной