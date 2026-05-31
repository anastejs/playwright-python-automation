# переписываем встроенные fixtures для изменения аргументов запуска браузера и browser context

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")    # fixture создаётся один раз на всю тестовую сессию
# переопределяем встроенную fixture browser_type_launch_args, которая отвечает за аргументы запуска браузера
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,   # взять все существующие настройки для запуска браузера
        "headless": False,        # добавляем свои настройки
        "slow_mo": 500,
    }

@pytest.fixture(scope="session")
# override built-in fixture, которая отвечает за аргументы запуска browser context
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        # создай browser context уже с сохранённой login/session информацией из файла storage_state.json
        "storage_state": "../playwright/.auth/storage_state.json",
        # то есть каждый новый context автоматически загружает cookies, login state и session из файла
    }


def test_page_has_docs_link(page: Page):
    page.goto("http://playwright.dev/python")
    docs_link = page.get_by_role("link", name="Docs")
    expect(docs_link).to_be_visible()

def test_visits_google_account(page: Page):
    page.goto("https://accounts.google.com")
    page.screenshot(path="account.jpg")