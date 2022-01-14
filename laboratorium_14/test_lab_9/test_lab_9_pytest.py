from zadanie_5 import fib, fill
import pytest


def test_fib():
    assert 3 == fib(3)
    with pytest.raises(TypeError):
        fib("TEST")


def test_fill():
    n = 2
    x = []
    for i in range(n):
        x.append([])
        for j in range(n):
            x[i].append(None)

    fill(x, n, n)

    for row in x:
        for element in row:
            if element is None:
                pytest.fail("Wynikowa lista nie jest uzupełniona do końca!")
