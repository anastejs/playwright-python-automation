# Page Object Model (POM) - шаблон проектирования для UI тестов, 
# который помогает организовать код и сделать его более поддерживаемым и читаемым.

# В Playwright Page Object Model clean API нужна для того, чтобы: скрывать сложную логику страницы,
# давать простые методы (login_page.login) вместо множества click/fill/locator, для упрощения сложных взаимодействий между авторами тестов.

from playwright.sync_api import Page


class LoginPage:

    # функция, которая запускается при создании объекта
    def __init__(self, page: Page):
        self.page = page     # page — это вкладка браузера из Playwright, сохраняем page
        self.page.goto("http://uitestingplayground.com/sampleapp")

        # Найдем нужные элементы на странице 
        self.username_input = self.page.get_by_placeholder("User Name")
        self.password_input = self.page.get_by_placeholder("********")
        self.login_btn = self.page.get_by_role("button", name="Log In")
        self.label = self.page.locator("label#loginstatus")     # текст, статус логина


    def login(self, username, password):     # передаем username и password в функцию
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()