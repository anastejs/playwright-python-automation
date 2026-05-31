# page.route() — это механизм для перехвата и управления HTTP requests браузера

from playwright.sync_api import Route, Page, expect
# Route - перехват HTTP запросов

# Handler function
def on_route(route: Route):
    # print("Request aborted:", route.request)
    # # блокирует request - браузер не отправит его на сервер
    # route.abort()

    # сценарий 3 - не загрузятся все изображения
    if route.request.resource_type == "image":
        route.abort()
    else:
        route.continue_()
    
def test_page_has_docs_link(page: Page):
    page.route(
        # сценарий 1 - все загрузится кроме logo.svg
        # "https://playwright.dev/python/img/playwright-logo.svg",

        # сценарий 2 - не загрузятся все файлы .png
        # "**/*.png",

        # сценарий 3 - захватываем все возможные URL
        "**",
        on_route
    )

    page.goto("https://playwright.dev/python")
    # page.screenshot(path="route()-without-playwright-logo.jpg")
    # page.screenshot(path="route()-without-all-png-images.jpg", full_page=True)
    page.screenshot(path="route()-without-all-images.jpg", full_page=True)