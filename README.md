# playwright-python-automation

![Python](https://img.shields.io/badge/Python-3.13-B5D5F5?style=flat&logo=python&logoColor=555555)
![Playwright](https://img.shields.io/badge/Playwright-1.60-B5F5D5?style=flat&logo=playwright&logoColor=555555)
![pytest](https://img.shields.io/badge/pytest-9.0.3-F5D5B5?style=flat&logo=pytest&logoColor=555555)
![pytest-playwright](https://img.shields.io/badge/pytest--playwright-0.8.0-F5B5D5?style=flat&logo=pytest&logoColor=555555)
![pytest-html](https://img.shields.io/badge/pytest--html-4.2.0-D5B5F5?style=flat&logo=pytest&logoColor=555555)
![pytest-xdist](https://img.shields.io/badge/pytest--xdist-3.8.0-F5F5B5?style=flat&logo=pytest&logoColor=555555)
![PyInstaller](https://img.shields.io/badge/PyInstaller-6.20.0-B5F5F5?style=flat&logoColor=555555)
![requests](https://img.shields.io/badge/requests-2.34.2-F5B5B5?style=flat&logo=python&logoColor=555555)
![POM](https://img.shields.io/badge/Pattern-Page_Object_Model-D5F5B5?style=flat&logoColor=555555)
![Data-Driven](https://img.shields.io/badge/Pattern-Data_Driven-F5D5F5?style=flat&logoColor=555555)

A hands-on test automation project built with **Playwright + Python**, covering core QA engineering practices — pytest fundamentals, browser automation, parallel execution, HTML reporting, playwright's interactive REPL mode, API testing, Page Object Model, and much more.

> **Pytest —** чистый testing framework
>
> **Playwright —** это browser automation framework (и частично library), предназначенный для E2E/UI тестирования через управление реальными браузерами.

## 📁 Project Structure

```
playwright-python-automation/
├── 10_web-first_assertions_expect/   # web-first assertions - expect()
├── 11_small_tasks/                  
├── 13_page_object_model_pom/         # Page Object Model
│   ├── pages/
│   └── tests/
├── 15_api-testing/                   # API tests
├── pytest-playwright/                # test hooks, codegen, screenshots/video, trace generator, 
│                                       @pytest.mark.skip_browser/only_browser, context arguments,
│                                       playwright's fixtures, Browser vs Context vs Page, page.route(),
│                                       network events, optimization, python debugger breakpoint(), 
├───┐                                   device emulation, data-driven testing @pytest.mark.parametrize() 
│   ├── reports/
│   └── videos/
├── videos/
├── .gitignore
├── requirements.txt
└── README.md
```

## General project installation

```bash
# Clone the repository
git clone https://github.com/anastejs/playwright-python-automation.git
# или добавить точку в конце для клонирования файлов именно в эту локальную папку
# git clone https://github.com/anastejs/cubeit.git . 
cd playwright-python-automation

# Create and activate virtual environment
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass    # (optional) I needed this
venv\Scripts\activate       

# Install dependencies
pip install -r requirements.txt
playwright install        # скачивает бинарники браузеров
```

## 02 — Playwright's interactive mode REPL (notes)

В терминале задаем команду:

```bash
python
```

Далее используем интерактивный режим:
```python
from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False, slow_mo=500)
page = browser.new_page()
page.goto(url)

# ...
# правильное завершение
browser.close()
playwright.stop()
exit()
```

## 06 — Playwright: глобальная установка (notes)

С компьютера вне виртуальной среды зайти в обычный терминал:

```bash
pip install playwright
playwright install                      # скачивает бинарники браузеров
$env:PLAYWRIGHT_BROWSER_PATH = "..."    # (не смогла сделать)
```

В папке самого проекта, находясь в виртуальной среде:

```bash
pip install pyinstaller
pyinstaller 06_automated_mail_checker.py --onefile
# (после этого в проекте появятся новые папки и файлы, build и .spec можно удалить)
# ! перенести .exe файл из папки dist в общий проект и удалить папку dist
.\test.exe       # запуск с самого терминала
```

## 07 — Установка pytest (notes)

Установка pytest с терминала, находясь в общей папке проекта в виртуальной среде (venv):

```bash
pip install pytest
pytest --version
pytest test_utils.py        # обычный запуск
pytest -v test_utils.py     # запуск с дополнительной информацией
pytest -s test_utils.py     # по умолчанию pytest не выписывает строки print(), -s - выводит в терминале
```

## 08 — Работа с плагином playwright (notes)

Одно из главных удобств Playwright pytest плагина, что он автоматически:
- запускает browser,
- создаёт context,
- создаёт page,
- закрывает всё после теста.
   
```bash
pip install pytest-playwright           # плагин playwright для pytest

# как запускать?
pytest test.app или pytest или pytest --headed --slowmo=500
pytest --headed --browser=firefox --slowmo=500
pytest -k test_root                     # запустить один определенный тест
pytest --device="iPhone 14 Pro Max"     # протестить на определенном девайсе
pytest --tracing on
pytest --tracing off
pytest --tracing retain-on-failure      # включить tracing для провальных тестов 
                                        # (сохраняется в папке test-results)
pytest --video on                       # создание видео теста (сохраняется в папке test-results)
pytest --screenshot on                  # создание скриншота после выполнения теста
pytest --screenshot-only-on-failure     # создание скриншота при провальном тесте
```

Создать **файл с конфигурацией `pytest.ini`**, содержание например:

```ini
[pytest]
addopts = --headed --slowmo=500
```

## 09 — Playwright Codegen (notes)

Playwright Codegen — это инструмент, который автоматически генерирует Playwright-код по твоим действиям в браузере (клики, ввод текста, переходы и т.д.)

чтобы запустить -> в терминале команда:

```bash
playwright codegen playwright.dev
```

## 16 — Запуск параллельного выполнения тестов (notes)

Быстрее и оптимизированее.

```bash
pip install pytest-xdist      # установка плагина внутри venv
pytest --numprocesses auto    # (рекомендуется) сам решает, сколько процессов (workers) использовать 
                              # (обычное значение = количество CPU)
pytest -n 3                   # запустить тесты в 3 параллельных процессах (workers)
```

## 17 — Создание HTML-reportов (notes)

HTML Report — это отчёт о результатах выполнения тестов в виде HTML-страницы, которую можно открыть в браузере.
Содержит количество тестов, Passed/Failed/Skipped, время выполнения, ошибки и stack trace, иногда скриншоты и логи.

```bash
pip install pytest-html                 # установка плагина pytest-html
pytest test_08_app_fixture.py --html=reports/report.html
pytest . --html=reports/report.html     # для всех тестов сразу
```

Для создания `report.html` при каждом запуске pytest — можно добавить в файл `pytest.ini` следующую строчку:

```ini
addopts = --html=reports/report.html
```
