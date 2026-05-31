# Mock API — перехват запроса и изменение ответа, чтобы тестировать поведение системы без изменения реального сервера

from playwright.sync_api import *


# функция вызавется, когда API запрос будет перехвачен
def on_api_call(route: Route):
    response = route.fetch()          # оригинальный API запрос и получение реального ответа
    user_data = response.json()       # JSON-ответ сервера -> в Python-словарь (dict)

    user_data["lastName"] = "Cherry"  # Меняем данные (MOCK)
    user_data["age"] = 17

    route.fulfill(
        response=response,
        json=user_data,
    )


def test_user_api(page: Page):
    USERS_API_URL = "https://dummyjson.com/users/1"   # API, которое будем перехватывать

    page.route(USERS_API_URL, on_api_call)            # когда браузер пойдёт на этот URL → вызовется on_api_call

    response = page.goto(USERS_API_URL)
    print("Got data:", response.json())               # уже изменённый ответ