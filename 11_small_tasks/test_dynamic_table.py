# Тест проверяет, что значение CPU для Chrome отображается правильно в динамической таблице.

from playwright.sync_api import Page, expect


def test_dynamic_table(page: Page):
    page.goto("http://uitestingplayground.com/dynamictable")
    
    # находим CPU value, который отображается под таблицей на сайте
    label = page.locator("p.bg-warning").inner_text()
    percentage = label.split()[-1]

    # находим все заголовки столбцов
    column_headers = page.get_by_role("columnheader")
    cpu_column = None

    # находим столбец с названием "CPU"
    for index in range(column_headers.count()):
        column_header = column_headers.nth(index)

        if column_header.inner_text() == "CPU":
            cpu_column = index
            break
    
    # make sure CPU column is found
    assert cpu_column != None

    # находим вторую группу rowgroup в таблице, потому что первая - это заголовок таблицы
    rowgroup = page.get_by_role("rowgroup").last
    # находим строку с названием "Chrome"
    chrome_row = rowgroup.get_by_role("row").filter(
        has_text="Chrome"
    )
    # находим ячейку в строке "Chrome" с индексом столбца "CPU"
    chrome_cpu = chrome_row.get_by_role("cell").nth(cpu_column)

    # expect given cpu value to match cell value
    expect(chrome_cpu).to_have_text(percentage)