# Тест проверяет видимость кнопок

import pytest
from playwright.sync_api import Page, expect, TimeoutError


def test_visibility(page: Page):
    page.goto("http://uitestingplayground.com/visibility")

    # "hide" button
    hide_button = page.get_by_role("button", name="Hide")

    # other buttons
    removed_button = page.get_by_role("button", name="Removed")
    zero_width_button = page.get_by_role("button", name="Zero Width")
    overlapped_button = page.get_by_role("button", name="Overlapped")
    opacity_0_button = page.get_by_role("button", name="Opacity 0")
    hidden_button = page.get_by_role("button", name="Visibility Hidden")
    display_none_button = page.get_by_role("button", name="Display None")
    offscreen_button = page.get_by_role("button", name="Offscreen")

    # hide all the buttons
    hide_button.click()

    # 1. check - button removed from dom
    expect(removed_button).to_be_hidden()

    # 2. check - button has zero width/height
    expect(zero_width_button).to_have_css("width", "0px")

    # 3. check - button is covered by other element
    with pytest.raises(TimeoutError):
        overlapped_button.click(timeout=2000)

    # 4. check - button opacity set to 0 (or visibility: hidden, or display: none)
    expect(opacity_0_button).to_have_css("opacity", "0")

    # 5. check - visibility set to hidden
    expect(hidden_button).to_be_hidden()
    # expect(hidden_button).to_have_css("visibility", "hidden")

    # 6. check - display set to none
    expect(display_none_button).to_be_hidden()
    # expect(display_none_button).to_have_css("display", "none")

    # 7. check - button is moved offscreen
    expect(offscreen_button).not_to_be_in_viewport()