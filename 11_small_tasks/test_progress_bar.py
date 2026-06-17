# Тест проверяет работу прогресс-бара

from playwright.sync_api import Page


def test_progressbar(page: Page):
    page.goto("http://uitestingplayground.com/progressbar")

    progressbar = page.get_by_role("progressbar")
    start_btn = page.get_by_role("button", name="Start")
    stop_btn = page.get_by_role("button", name="Stop")

    # start progress bar
    start_btn.click()

    # check progress
    while True:
        valuenow = int(progressbar.get_attribute("aria-valuenow"))
        print(f"Percent: {valuenow}%")

        # progress more than or equal to 75
        if valuenow >= 75:
            break

    # stop progress bar
    stop_btn.click()

    assert valuenow >= 75

# pytest test_progress_bar.py -s