import re      #регулярные выражения
from playwright.sync_api import Page, expect

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    docs_link = page.get_by_role("link", name="Docs")

    # ожидается именно такое значение атрибута class
    expect(docs_link).to_have_class("navbar__item navbar__link")
    
    # ожидается, что class содержит значение
    expect(docs_link).to_have_class(re.compile(r"navbar__link"))  #теперь можно использовать любые регулярные выражения

    # expect id (у данной ссылки нету id, поэтому закомментировано)
    # expect(locator).to_have_id("value")

    # проверяем, что атрибут href существует и не пустой (содержит хотя бы один символ)
    expect(docs_link).to_have_attribute("href", re.compile(".+")) 

    # expect attribute and value in locator
    expect(docs_link).to_have_attribute("href", "/python/docs/intro")