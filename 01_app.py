# Полностью пустой новый проект -  с чего начать?
# В терминале ввести команду: python -m venv venv
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass   (каждый раз когда закрываю и заново захожу нужно запускать)
# venv\Scripts\activate
# pip install playwright     
# playwright --version   # проверка
# playwright install  (иногда у меня ниичего не происходит, значит браузеры для Playwright уже установлены)

# На будущее:
# pip install pytest 
# pip install pytest-playwright

# Советую для себя (можно сразу все за раз):
# pip install pytest playwright pytest-playwright

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #Lounch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    #Create a new page
    page = browser.new_page()
    #Visit the playwright website
    page.goto("https://playwright.dev/python")

    #Locate a link element with "Docs" text
    docs_button = page.get_by_role('link', name="Docs")
    docs_button.highlight()
    docs_button.click()
    #Get the url
    print("Docs:", page.url)

    browser.close()

# python 01_app.py