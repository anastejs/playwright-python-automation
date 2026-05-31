# page.route() — это механизм для перехвата и управления HTTP requests браузера

from playwright.sync_api import Route, Page, expect
# Route - перехват HTTP запросов


def on_route(route: Route):
    # сценарий 1 - кастомный response
    # route.fulfill(
    #     status=200,
    #     body="<html><body><h1>Custom Response!</h1></body></html>"
    # )

    # сценарий 2 - перехватываем response и меняем его
    print("ROUTE INTERCEPTED!")
    response = route.fetch()     # получаем реальный response
    original_body = response.text()
    body = original_body.replace(
        "Playwright",
        "SUPER PLAYWRIGHT"
    )
    # отправляем modified response в браузер
    route.fulfill(
        response=response,
        body=body,
    )

def block_js(route: Route):
    route.abort()

def test_page_has_docs_link(page: Page):

    page.route("https://playwright.dev/python", on_route)
    # блокируем JavaScript-файлы, чтобы React не перерисовал изменённый HTML (отключаем React hydration)
    page.route("**/*.js", block_js)

    page.goto("https://playwright.dev/python")
    page.pause()