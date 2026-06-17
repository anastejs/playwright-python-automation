from playwright.sync_api import sync_playwright

#закомментино из-за REPL
# with sync_playwright() as playwright:

# Playwright's interactive mode (REPL) через терминал
# python (в терминале)
playwright = sync_playwright().start()
#Lounch a browser
browser = playwright.chromium.launch(headless=False, slow_mo=500)
#Create a new page
page = browser.new_page()

#Additional from others websites - это нужно закоментировать
#url = "https://bootswatch.com/default"
#page.goto(url)
checkbox = page.get_by_role("checkbox", name="Default checkbox")
checkbox.highlight()
checkbox.check()
checkbox.is_visible()

page.get_by_role("button", name="Primary").locator("nth=0").highlight()
page.get_by_role("button", name="Primary").first.highlight()
page.get_by_role("button", name="Primary").last.highlight()
page.get_by_label("Password").highlight()
page.get_by_placeholder("Enter email").highlight()
page.get_by_text("Middle").click()
page.get_by_title("Source title").highlight()
#If text contains
page.get_by_text("fine print").highlight()
page.get_by_text("fine print", exact="True").highlight()
#For images - https://unsplash.com
page.get_by_alt_text("...").click()

#CSS SELECTORS
#with tag name
page.locator("h1").highlight()
page.locator("h1").locator("nth=12").highlight()
page.locator("footer").highlight()
#with class name
page.locator("button.btn-outline-success").highlight()
#with id
page.locator("button#btnGroupDrop1").click()
page.locator("id=btnGroupDrop1").highlight()
#with attribute name and its value
page.locator("input[readonly]").highlight()
page.locator("input[value='correct value']").highlight()
page.locator("li[data-tooltip='Mark as read']").highlight()
# with label and its id (example from another website)
page.locator("css=label#loginstatus")
# with class and text (example from another website)
page.locator("div.bg-primary").get_by_text("Welcome")

#parent child relationship
page.locator("nav.bg-dark a.nav-link.active").highlight()
#parent_tag.class child_tag.class1.class2
#try pseudo class visivle
page.locator("div.dropdown-menu:visible").highlight()
page.locator("div.dropdown-menu").locator("visible=true").highlight()

#Как выделить конкретный заголовок?
page.get_by_text("Navbars")
#или используя pseudo class :text
page.locator("h1:text('Navbars')").highlight()
#точный текст заголовка
page.locator("h1:text-is('Navbars')").highlight()
#pseudo class :nth-match()
page.locator(":nth-match(button.btn-primary, 4)").highlight()
page.locator(":nth-match(button:text('Primary'), 3)").highlight()

#XPath Locators
page.locator("xpath=//h1").highlight()
#with attributes
page.locator("xpath=//h1[@id='navbars']").highlight()
page.locator("//input[@readonly]").highlight()
page.locator("//input[@value='wrong value]").highlight()

#XPath Functions
#text() = 'находит точный текст'
page.locator("//h1[text() = 'Heading 1']").highlight()
#contains() = 'находит свободный текст'
page.locator("//h1[ contains(text(), 'Head') ]").highlight()
#найдем конкретный класс с помощью contains()
page.locator("//button[ contains(@class, 'btn-outline-primary') ]").highlight()
#найдем конкретный input с помощью contains() и его attribute
page.locator("//input[ contains(@value, 'correct') ]").highlight()

#Other locators
#Выбрать родителя
page.get_by_label("Email address").locator("..").highlight()
#Выбрать элемент на основе фильтра - текст
page.get_by_role("heading").filter(has_text="Heading").highlight()
#Выбрать элемент на основе фильтра - содержит ли он определенный элемент
page.locator("div.form-group").filter(has=page.get_by_label("Password")).highlight()

#Вывести отправителя и заголовок имейла
sender = email.locator("td span[email]:visible").inner_text()   
title = email.locator("td span[data-thread-id]:visible").inner_text()

#Для выбора надежных и устойчивых селекторов есть несколько СТРАТЕГИЙ:

# Использование атрибутов data-test (или аналогичных): Это, пожалуй, самый надежный способ. Разработчики специально добавляют такие атрибуты к элементам, чтобы их можно было легко найти в тестах, не привязываясь к CSS-классам или структуре DOM, которые могут часто меняться.
# Пример: <button data-test="submit-button">Отправить</button>
# Селектор: page.locator('[data-test="submit-button"]')

# Использование явных текстовых селекторов: Playwright позволяет искать элементы по их видимому тексту. Это хорошо, потому что текст обычно меняется реже, чем CSS-классы.
# Пример: page.locator('text=Отправить')

# Использование ролей доступности (ARIA roles): Это также очень надежный способ, так как роли предназначены для обеспечения доступности и редко меняются.
# Пример: page.getByRole('button', name='Отправить')

# Избегание хрупких селекторов: Старайтесь не использовать селекторы, основанные на:
# CSS-классах, которые генерируются динамически или часто меняются (например, class="sc-123abc").
# Порядке элементов (например, div:nth-child(2)), так как порядок может легко измениться.
# Глубоких вложенностях (например, body > div > main > section > div > div > button), так как это делает селектор очень чувствительным к изменениям в структуре DOM.