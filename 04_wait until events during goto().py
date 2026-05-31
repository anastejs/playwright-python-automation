#wait_until=''
from playwright.sync_api import sync_playwright
from time import perf_counter


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    print("Page loading...")
    start = perf_counter()

    page.goto(
        "https://playwright.dev/python/",
        # Response received - сразу после получения html-ответа от сервера, не дожидаясь отображения в браузере
        # wait_until='commit',

        # HTML parsed and <script> executed - загрузка html только с текстом и js, без картинок и медиа 
        # wait_until='domcontentloaded',

        # Default, HTML loaded along with resources - загрузка со всеми медиа с сайта
        wait_until='load',

        # Network operations stopped - когда сеть становится неактивной: то есть после загрузки html, еще грузятся и обрабатываются сетевые запросы в фоновом режиме (напр. аналитика)
        # wait_until='networkidle',
    )

    time_taken = perf_counter() - start
    print(f"...Page loaded in {round(time_taken, 2)}s")
    
    browser.close()