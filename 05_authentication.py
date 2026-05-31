from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:

    # browser = playwright.chromium.launch(executable_path=r"C:\Users\20anv\AppData\Local\Programs\Opera\opera.exe", headless=False, slow_mo=500)
    browser = playwright.chromium.launch(
        headless=False, slow_mo=500,
        # проблема - "Возможно, этот браузер или приложение небезопасны.." решение ниже
        args=["--disable-dev-shm-usage", "--disable-blink-features=AutomationControlled"]
        )
    # Context - изолированная браузерная сессия/среда со своими cookies, localStorage, sessionStorage, авторизацией и вкладками, page - конкретная вкладка
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://accounts.google.com")
    # Enter email address
    email_input = page.get_by_label("Телефон или адрес эл. почты")
    email_input.fill("20anv07@gmail.com")
    page.get_by_role("button", name="Далее").click()

    # Enter password
    password_input = page.get_by_label("Введите пароль")
    password_input.fill("nastycomua")
    page.get_by_role("button", name="Далее").click()

    # Pause if your account has two-factor authentication
    # then complete the same before resuming
    page.pause()

    # Save authentication state
    context.storage_state(
        path="playwright/.auth/storage_state.json",
	# make sure you've created the playwright/.auth directory в этой папке проекта!
    )

    #при повторной авторизации - нам уже не нужно вводить логин/пароль, а только подтянуть сохраненные данные из json
    # context = browser.new_context(
    #     storege_state = "playwright/.auth/storage_state.json"
    # )

    context.close()