# CRUD je základný súbor operácií nad dátami v API alebo databáze: vytvorenie (Create), čítanie (Read), 
# aktualizácia (Update) a odstránenie (Delete). Používa sa na základnú prácu s entitami v systéme v rámci REST API.

# REST API je architektonický štýl webových služieb, kde klient komunikuje so serverom prostredníctvom HTTP požiadaviek 
# (GET, POST, PUT, DELETE) na prácu s jednotlivými zdrojmi (entitami) v systéme.

import pytest
from playwright.sync_api import *


# пример 1 вариант 1 - через page.goto(), который не предназначен для API testing, хорош для UI тестов
def test_users_api(page: Page):
    # используем browser page, то есть запускается реальный браузер -> происходит HTTP request -> Playwright возвращает response объекта страницы
    response = page.goto("https://dummyjson.com/users/1")     # API Call

    user_data = response.json()
    # print(user_data)

    assert "firstName" in user_data
    assert "lastName" in user_data

    assert user_data["firstName"] == "Emily"
    assert user_data["lastName"] == "Johnson"


# пример 1 вариант 2 - правильный API testing (тоже самое, но лучше использовать APIRequestContext)
# Python → HTTP request → API server → response, без браузера вообще (он даже не открывается)

def test_users_api_request_context(playwright: Playwright): 
    api_context = playwright.request.new_context(base_url="https://dummyjson.com")

    response = api_context.get("users/1")   # API Call - отправляем GET запрос

    user_data = response.json()             # JSON-ответ сервера -> в Python-словарь (dict)
    # print(user_data)                      # вывести весь найденный dict

    assert "firstName" in user_data
    assert "lastName" in user_data

    assert user_data["firstName"] == "Emily"
    assert user_data["lastName"] == "Johnson"

    api_context.dispose()                   # нужно обязательно закрыть соединение api_context



# пример 2 - GET - READ: поиск пользователей по первому имени

@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    #создаём новый API клиент (контекст), через который будем делать HTTP запросы:
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com",
        extra_http_headers={'Content-Type': 'application/json'},  # говорим серверу: я отправляю JSON данные (для POST и UPDATE)
        )
    yield api_context
    api_context.dispose()   # нужно обязательно закрыть соединение api_context

def test_users_search(api_context: APIRequestContext):
    query = "Jack"                                           # поиск пльзователей
    response = api_context.get(f"/users/search?q={query}")   # API Call - отправляем GET запрос

    users_data = response.json()    # JSON-ответ сервера -> в Python-словарь (dict)
    # print(users_data)             

    # дальше для себя: можно закомментить
    matched_users = []
    print(f"{users_data["total"]} users found matching the search '{query}'")   # сколько пользователей нашло

    for user in users_data["users"]:
        # print(user["firstName"], user["lastName"])

        if query.lower() in user["firstName"].lower():  # сравнение текста в поиске с первым именем пользователя
            matched_users.append(user)

    # check that at least one user matches the search query
    assert matched_users, f"No users found with name containing '{query}'"

    # тут уже можно раскомментить
    assert any(                                         # проверка всего словаря users_data
        query.lower() in user["firstName"].lower()      # сравнение текста в поиске с первым именем пользователя
        for user in users_data["users"]                 # для всех найденных пользователей из json списка users_data
    ), f"No users found with name containing '{query}'"


# пример 3 - POST - CREATE нового пользователя
def test_create_user(api_context: APIRequestContext):
    response = api_context.post(      # API Call - отправляем POST запрос
        "users/add",                  # endpoint (добавится к base_url)
        data={                        # тело запроса (payload)
            "firstName": "Nastia",
            "lastName": "Cherry",
            "age": 24
        }
    )
    user_data = response.json()       # JSON-ответ сервера -> в Python-словарь (dict)
    # print(user_data)

    assert user_data["id"] == 209     # всего 208 пользователей, создаем 209го
    assert user_data["firstName"] == "Nastia"


# пример 4 - PUT - UPDATE данных 1. пользователя
def test_update_user(api_context: APIRequestContext):
    # до обновления: отправляем GET запрос - получить фамилию 1. пользователя
    # print("Default Last Name:", api_context.get("users/1").json()["lastName"])
    response = api_context.put(     # API Call - отправляем PUT запрос "перезаписать данные"
        "users/1",                  # endpoint пользователя с id=1
        data={
            "lastName": "Cherry",
            "age":  17,
        }
    )
    user_data = response.json()     # JSON-ответ сервера -> в Python-словарь (dict)
    # print(user_data)

    assert user_data["lastName"] == "Cherry"
    assert user_data["age"] == 17


# пример 5 - DELETE данных 1. пользователя
def test_remove_user(api_context: APIRequestContext):
    # API Call - отправляем DELETE запрос: удалить пользователя с id = 1
    response = api_context.delete("users/1")   
    user_data = response.json()          # JSON-ответ сервера -> в Python-словарь (dict)
    # print(user_data)
    assert user_data["isDeleted"] is True


# pytest test_api.py -s