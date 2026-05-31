from playwright.sync_api import Locator, Page, expect
# Locator - для использования в функции def search_results(self) -> Locator

class PlaywrightPage:

    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://playwright.dev/python")   
        # Найдем нужные элементы на странице
        self.docs_link = self.page.get_by_role("link", name="Docs")
        self.search_input = self.page.get_by_placeholder("Search docs")


    def visit_docs(self):
        self.docs_link.click()

    def search(self, query):  
        self.page.keyboard.press("Control+KeyK")
        self.search_input.fill(query)
        
    def search_results(self) -> Locator:
        print("Search Results:")
        for result in self.page.locator("span.DocSearch-Hit-title").all():
            print(result.inner_text())

        # была проблема - Locator expected to be visible (этот locator unstable - он появляется, но не всегда)
        # return self.page.locator("div.DocsSearch-Dropdown")    
        return self.page.locator(".DocSearch-Container")      # вернем окно с результатами поиска
