# основа кода
from playwright.sync_api import Page

# чтобы запустить Codegen -> в терминале команда: playwright codegen playwright.dev

# сюда вставить сгенерированный код с Codegen:

def test_example(page: Page) -> None:   # это строка означает, что pytest сам создаст browser/context/page перед тестом и сам всё закроет после теста
    page.goto("https://playwright.dev/")
    page.get_by_text("Node.jsNode.jsPythonJava.NET").click()
    page.get_by_label("Main", exact=True).get_by_role("link", name="Python").click()
    page.get_by_role("button", name="Search (Ctrl+K)").click()
    page.get_by_role("searchbox", name="Search").fill("Codegen")
    page.get_by_role("searchbox", name="Search").press("Enter")
    page.get_by_role("button", name="Copy code to clipboard").click()
    page.get_by_role("link", name="Previous « Writing tests").click()

