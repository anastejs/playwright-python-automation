import json

def generate_report():
    # generate report data
    dictionary = {
        "timestamp": "2023-4-27 12-37-9",    #время создания отчёта
        "status": "PASSED",                  #статус теста
        "summary": "module.py::test_case"    #какой тест запускался
    }
    # open json file in writing mode
    with open("report.json", "w") as file:
        # write data to json file
        json.dump(dictionary, file)