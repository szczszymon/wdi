from zadanie_9 import factorize, print_res
import pytest


@pytest.fixture
def factor_result():
    result = []
    factorize(4, result, [], 0, 1)
    return result


def test_factorize(factor_result):
    assert [1, 1, 2] in factor_result


@pytest.fixture
def factor_str(factor_result):
    return print_res(factor_result)


@pytest.fixture
def plus_sum(factor_str):
    suma = 0
    for element in factor_str:
        if element == "+":
            suma += 1
    return suma


@pytest.fixture
def digit_sum(factor_str):
    suma = 0
    for element in factor_str:
        if element in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            suma += 1
    return suma


def test_result(plus_sum, digit_sum):
    assert digit_sum > plus_sum
