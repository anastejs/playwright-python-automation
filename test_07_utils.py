import utils_07

def test_root():
    root_25 = utils_07.root(25)
    # assert - я ожидаю, что это истина, иначе это баг
    assert root_25 == 5