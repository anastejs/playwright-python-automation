from playwright.sync_api import sync_playwright

# playwright = sync_playwright().start()    #for REPL
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        # нужно было для запуска .exe из терминала
        executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        # executable_path=r"C:\Users\20anv\AppData\Local\Programs\Opera\opera.exe",
        headless=False, slow_mo=500,
        # проблема - "Возможно, этот браузер или приложение небезопасны.." решение ниже
        args=["--disable-dev-shm-usage", "--disable-blink-features=AutomationControlled"]
        )
    context = browser.new_context(
        storage_state="playwright/.auth/storage_state.json"
    )
    page = context.new_page()
    page.goto("https://gmail.com")

    # КОСТЫЛЬ - если браузер открывает "Выберите аккаунт"
    page.locator("div[data-email='20anv07@gmail.com']").click()
    password_input = page.get_by_label("Введите пароль")
    password_input.fill("nastycomua")
    page.get_by_role("button", name="Далее").click()
    page.pause()
 
    new_emails = []   # список новых мейлов
    # выделяем таблицу - все мейлы в нашей почте
    emails = page.locator("div.UI table tr")
    # emails.highlight()

    # просто проверка работает ли
    # third_email = emails.nth(2)
    # third_email.locator("li[data-tooltip='Отметить как непрочитанное']").highlight()

    for email in emails.all():     # проходимся по всем письмам
        # проверяем новое ли это письмо по присутствию атрибута data-tooltip='Mark as read' в письме
        is_new_email = email.locator(
            "td li[data-tooltip='Отметить как прочитанное']"
        ).count() == 1

        # если у нас действительно новое письмо:
        if is_new_email:
            sender = email.locator("td span[email]:visible").inner_text()           # находим кто отправил
            title = email.locator("td span[data-thread-id]:visible").inner_text()   # находим заголовок письма

            # добавляем в список новое письмо
            new_emails.append(
                [sender, title]
            )

    # проверяем, сколько у нас появилось новых писем
    if len(new_emails) == 0:
        print("No new emails!")
    else:
        print(f"You have {len(new_emails)} new email(s)!")
        print("-"*30)    #просто для декорации

        for new_email in new_emails:
            print(new_email[0]+":", new_email[1])
            print("-"*30)      #просто для декорации

    context.close()

