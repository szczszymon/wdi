from zadanie_8 import check_parentheses, drop_different
import pytest


def test_parentheses():
    assert check_parentheses("()())()") is True
    assert check_parentheses("()()()") is False


def test_drop():
    data = "(test)"
    data = drop_different(data)
    if "test" in data:
        pytest.fail("Znaleziono znaki inne niż ( i ) w outpucie")
