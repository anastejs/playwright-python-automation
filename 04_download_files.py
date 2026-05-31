# expect_download(), save_as(), page.once()

from playwright.sync_api import sync_playwright

# download event handler - вариант 2
def on_download(download):
    print("Download received!")
    download.save_as("night.jpg")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    page = browser.new_page()
    page.goto("https://unsplash.com/photos/NDRwHCC7JuI")

    # register listener, once() потому что используем один раз - вариант 2
    page.once("download", on_download)

    btn = page.get_by_role("link", name="Download free")

    # expect download
    with page.expect_download() as download_info:
        # trigger download
        btn.click()

    # Save using download_info - вариант 1
    # download = download_info.value
    # download.save_as("moon.jpg")

    browser.close()