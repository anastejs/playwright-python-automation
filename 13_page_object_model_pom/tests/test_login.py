from pages.login_page import LoginPage
from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    username = 'dan'
    password = 'pwd'

    login_page = LoginPage(page)     # создаем объект страницы логина
    login_page.login(username, password)     # вызываем функцию login(), передаем username и password
    # проверка - текст статуса логина (login_page.label) будет "Welcome, {username}!"
    expect(login_page.label).to_have_text(f"Welcome, {username}!")

def test_failed_login(page: Page):
    username = 'dan'
    password = 'wrong_password'

    login_page = LoginPage(page)
    login_page.login(username, password)
    # проверка - текст статуса логина (login_page.label)будет "Invalid username/password"
    expect(login_page.label).to_have_text("Invalid username/password")