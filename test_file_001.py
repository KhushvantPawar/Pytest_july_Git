

import allure
import pytest

from selenium import webdriver

# pip install allure-pytest - to generate allure report
class Test_Credence_001:
    def test_sum_001(self):
        a=10
        b=20
        sum = a+b
        print("sum of a and b is ",sum)
        if sum ==30:
            assert True
        else:
            assert False

    def test_CredenceUrl_002(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("You are at credence.in")
            assert True
            driver.close()
        else:
            print("You are at Wrong url")
            driver.close()
            assert False



