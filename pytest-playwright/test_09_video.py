import pytest       #для создания fixture 
from playwright.sync_api import Browser, Page   #Page - чтобы появилась подсказка для page, Browser - для создания context

DOCS_URL = "https://playwright.dev/python/docs/intro"

@pytest.fixture 
def recordable_page(browser: Browser):
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()
    yield page     #перед тестом выполняется код до yield, после теста выполняется код после yield
    context.close()

def test_get_started_visits_docs(recordable_page: Page):
    page = recordable_page
    page.goto("https://playwright.dev/python")
    theme_btn = page.get_by_title("system mode")
    theme_btn.dblclick()  
    link = page.get_by_role("link", name="Get started")
    link.click()

    assert page.url == DOCS_URL 