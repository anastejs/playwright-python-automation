# Иногда текст содержит неразрывные пробелы (NBSP) для того, чтобы предотвратить переход на новую строку при уменьшении экрана,
# они мешают поиску по тексту, поэтому используют unicode-символ пробела \u00a0

import pytest
from playwright.sync_api import Page, TimeoutError


def test_nbsp(page: Page):
    page.goto("http://uitestingplayground.com/nbsp")
    
    # using normal space - this will raise a TimeoutError
    with pytest.raises(TimeoutError):
        page.locator("//button[text()='My Button']").click(
            timeout=2000
        )
    # using non-breaking space (NBSP character)
    page.locator("//button[text()='My\u00a0Button']").click()