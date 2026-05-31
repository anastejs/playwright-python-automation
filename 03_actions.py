from playwright.sync_api import sync_playwright

#закомментино из-за REPL
# with sync_playwright() as playwright:

# Playwright's interactive mode (REPL) через терминал
playwright = sync_playwright().start()
#Lounch a browser
browser = playwright.chromium.launch(headless=False, slow_mo=500)
#Create a new page
page = browser.new_page()
url = "https://bootswatch.com/default"
page.goto(url)

#Actions with buttons
button = page.get_by_role("button", name='Block button').first
outline_button = page.locator("button.btm-outline-primary")

button.click()
button.dblclick(delay=500)
button.click(button="right")
button.is_enabled()     #активна ли кнопка
#Комбинация клавиш с кликом мышкой
button.click(modifiers=["Shift", "Control", "Alt"])
outline_button.hover()

#Actions with input
#Передвигаем мышку на конец странички, чтобы потом выбрать последнюю форму ввода
page.locator("footer").highlight()
input = page.get_by_placeholder("Enter email")
#Ввести данные в поле ввода
input.fill("me@gmail.com")
input.clear()
#Задержка между написанием букв, иммитация человека
input.type("me@gmail.com", delay=200)
#Извлечь данные из поля ввода
valid_input = page.get_by_label("Valid input").first
valid_input.input_value()

#Radios
radio_option1 = page.get_by_label("Option one is this and that—be sure to include why it's great")
radio_option2 = page.get_by_label("Option two can be something else and selecting it will deselect option one")
radio_option2.check()

#Checkboxes
checkbox = page.get_by_label("Default checkbox")
checkbox.check()
checkbox.uncheck()
#или
checkbox.click()
#Проверка
checkbox.is_checked()
checkbox.set_checked(True)
checkbox.set_checked(False)

#Switches
switch = page.get_by_label("Checked switch checkbox input")
switch.uncheck()
switch.check()

#Select options
select = page.get_by_label("Example select")
select.select_option("4")

multi_select = page.get_by_label("Example multiple select")
multi_select.select_option(["2", "4"])

#Выбрать ссылку в выпадающем меню
dropdown = page.locator("button#btnGroupDrop1")
dropdown.click()
dropdown_link = page.locator("div.dropdown-menu:visible a:text('Dropdown link')").last
dropdown_link.click()

#Upload files
file_input = page.get_by_label("Default file input example")
#если принимает много файлов
# file_input.set_input_files(["01_app.py", "02_locators.py"])
file_input.set_input_files("01_app.py")
#если нужно выбрать файл с компьютера
with page.expect_file_chooser() as fc_info:
    file_input.click()
file_chooser = fc_info.value
file_chooser.set_files("01_app.py")

#Заполнение поля textarea
textarea = page.get_by_label("Example textarea")
textarea.fill("word")
textarea.clear()
#Имитация написания букв
textarea.press("Shift+KeyW")
textarea.press("KeyO")
textarea.press("KeyR")
textarea.press("KeyD")
textarea.press("Control+ArrowLeft")