# Data-Driven Testing (DDT) - подход в тестировании, при котором входные данные отделены от логики теста
# и подставляются из внешнего источника (CSV, Excel, JSON, базы данных, параметров pytest и тд.)
# Основная идея - один тест → много наборов данных → много проверок
# недостатки: слишком большие наборы данных → тесты выполняются долго, сложность в поддержке тестов, сложнее дебажить

import pytest
from parametrize_20_calc_root import root

# тут входныеданные находятся в () в виде tuple
# также могут быть в [] в виде list списка
@pytest.mark.parametrize(("input_num, output_num_root"), (
        (100, 10),
        (36, 6),
        (25, 5),
        (16, 4),
        (9, 3),
        (4, 2),
    )
)

def test_root(input_num, output_num_root):
    assert root(input_num) == output_num_root

# pytest test_20_root_with_parametrize.py -v