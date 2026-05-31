# эмуляция различных устройств и свойств браузера для тестирования

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)

    device_args = playwright.devices["iPhone 14 Pro"]

    # выбор device для context
    # context = browser.new_context(**device_args)

    # custom viewport (custom device) + настройки браузера
    context = browser.new_context(
        is_mobile=True,
        has_touch=True,
        viewport={"width": 300, "height": 500},
        color_scheme="dark",
        permissions=["geolocation", "camera", "microphone"],
        geolocation={"latitude": 48.1486,"longitude": 17.1077}
    )

    page = context.new_page()
    page.goto("https://playwright.dev/python")
    page.get_by_role("link", name="GET STARTED").click()

    # тут также можно менять viewport
    page.set_viewport_size({"width": 1000, "height": 1000})

# python 17_device_emulation.py