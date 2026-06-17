import json
import report_07
import pytest

#создаём фикстуру, которая будет выполняться один раз для всех тестов в течении одной сессии (одного запуска pytest)
# primary use of a pytest fixture in testing - is to share test data between tests

#scope="function" - по умолчанию, выполняется для каждой отдельной функции (каждого теста)
#scope="module" - выполняется один раз для всех тестов в одном файле
@pytest.fixture(scope="session")      
def report_json():
    print("\n[ Fixture ]: requested...")
    report_07.generate_report()     #запускаем функцию генерации отчёта, которая создаёт json файл с данными

    with open("report.json") as file:
        print("[ Fixture ]: ...return report data")
        return json.load(file)     #загружаем данные из json файла в python словарь, возвращаем его в тесты

def test_report_json(report_json):
    print("[ Test ]: recieved -", report_json)
    assert type(report_json) == dict

def test_report_json_keys(report_json):
    print("[ Test ]: recieved -", report_json)
    assert "timestamp" in report_json
    assert "status" in report_json
    assert "summary" in report_json

#в терминале pytest -v -s test_report_07.py