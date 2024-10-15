###  Python API Automation Framework

Tech Stack
- Python 3.12
- Requests : HTTP Requests
- Pytest : Testing framework
- Reporting : Allure report, pytest HTML
- Test Data : CSV, Excel, JSON, Faker
- Advance API testcase : Jsonschema
- Parallel Execution: x distribute (xdist)

-How to install packages
'''
pip install pytest requests pytest-html faker allure-pytest jsonschema
'''

-How to run testcase parallely
''' pip install pytest-xdist '''

-How to run basic testcase with allure report
''' pytest test/src/crud/test_lab001.py --allure_dir == allure-result -s '''

