#creating a dummy test to verify that everythig in this framework will be working fine

import pytest
import allure

@allure.title("Smaple test case")
def test_sample():
    assert True == True

