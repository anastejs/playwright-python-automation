# подсказки для других пользователей какого типа данные ожидается в переменной
# (просто доп инфа на будущее)
num: int = 100
lst: list[int] = [1, 2, 3, 4]
dictionary: dict[str, int] = {"key1": 0}

def root(num: int) -> float:
    return pow(num, .5)
# return 0   #failed test

