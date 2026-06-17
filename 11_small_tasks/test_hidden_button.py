# Тест проверяет, что кнопка "greenButton" становится недоступной после первого клика
# (в примере зеленая кнопка перекрывается синей кнопкой с более высоким Z-индексом)
# если элемент перекрыт, Playwright выбрасывает ошибку таймаута, сигнализируя, что клик невозможен
# если ожидаемая ошибка -> тест успешен

import pytest
from playwright.sync_api import TimeoutError, Page


def test_hidden_layer(page: Page):
    page.goto("http://uitestingplayground.com/hiddenlayers")

    green_btn = page.locator("button#greenButton")
    # click once
    green_btn.click()
    # clicking twice should raise error
    with pytest.raises(TimeoutError):
        green_btn.click(timeout=2000)