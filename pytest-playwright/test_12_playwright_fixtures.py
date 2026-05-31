# В Playwright такая иерархия:
# Browser
#    └── Context
#            └── Page

# Browser создаёт Context:      context = browser.new_context()
# Context создаёт Page:         page = context.new_page()

# (page: Page) vs (context: BrowserContext) - два разных способа доступа к браузерной сессии в тестах



from playwright.sync_api import *


DOCS_URL = "https://playwright.dev/python/docs/intro"

# Первый тест — более низкий уровень, дополнительно дается доступ к браузерной сессии
# Мы сами создаем новую страницу  из context (целая browser session, из которой можно: 
# создавать новые страницы (multiple tabs), управлять cookies и permissions, хранит login state)
def test_page_has_docs_link(context: BrowserContext):
    # context.add_cookies()
    # context.grant_permissions('geolocation')
    page = context.new_page()

    page.goto("https://playwright.dev/python")
    docs_link = page.get_by_role("link", name="Docs")
    expect(docs_link).to_be_visible()


# Тут pytest + Playwright автоматически: создают browser - создают context - создают page - передают page в тест
# Playwright сам создал page, мы просто используем его в тесте, не заботясь о том, как он создается и закрывается
# Тут мы работаем только с готовой вкладкой браузера

# Когда используется? Чаще всего для UI тестов, когда нам не нужно управлять браузерной сессией
def test_get_started_visits_docs(page: Page):
    page.goto("https://playwright.dev/python")
    page.get_by_role("link", name="Get started").click()
    expect(page).to_have_url(DOCS_URL)

# ----------------------------------------------------------------------------------------------
# 2. видео

# browser: Browser - это весь запущенный браузер целиком, хранит browser process, engine, memory/process level stuff
# Когда используется? Редко, когда нужно вручную создавать contexts, advanced setup, multi-user scenarios (тест двух пользователей одновременно)

# Все эти параметры (browser, playwright, browser_type..) — это готовые fixtures от Playwright pytest plugin, 
# которые pytest автоматически создаёт и передаёт в тест.
def test_page_has_docs_link(
        playwright: Playwright, # главный объект Playwright, пример: playwright.chromium, playwright.firefox
        browser: Browser, # запущенный браузер, пример: context = browser.new_context()
        browser_type: BrowserType, # тип браузера, пример: browser_type = playwright.chromium
        browser_name: str,    # строка, пример: "chromium", "firefox", "chromium-headless-shell"
        browser_channel: str,   # строка, конкретный browser channel/build, пример: "chrome", "msedge", "chrome-beta"
        is_firefox: bool):   # True если тест запущен в Firefox, иначе False
    
    page = browser.new_page()

    # просто пример использования
    if browser_name == playwright.chromium.name:
        print("This test is running in Chromium")
    elif browser_name == playwright.firefox.name:    # if browser_name == "firefox":
        print("This test is running in Firefox")

    page.goto("https://playwright.dev/python")
    docs_link = page.get_by_role("link", name="Docs")
    expect(docs_link).to_be_visible()

# тот же браузер, что создали в первой функции, но уже новая вкладка
def test_get_started_visits_docs(browser, page: Page):    
    page.goto("https://playwright.dev/python")
    page.get_by_role("link", name="Get started").click()
    expect(page).to_have_url(DOCS_URL)

#в терминале
#pytest
#pytest --headed --slowmo=500