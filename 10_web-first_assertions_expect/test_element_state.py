from playwright.sync_api import Page, expect

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    get_started_link = page.get_by_role("link", name="GET STARTED")

    # expect element visible виден
    expect(get_started_link).to_be_visible()
    # expect element enabled включен
    expect(get_started_link).to_be_enabled()
    
    get_python_link = page.get_by_role("link", name="Get Python")
    # expect element hidden спрятан
    expect(get_python_link).to_be_hidden()
    # тоже самое - ожидается, элемент не виден, но не проверяет, что он спрятан, может быть просто не существует
    expect(get_python_link).not_to_be_visible()