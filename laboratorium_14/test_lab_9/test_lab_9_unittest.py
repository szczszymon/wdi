from zadanie_5 import fib, fill
import unittest


class TestFib(unittest.TestCase):
    def test_number(self):
        self.assertEqual(fib(3), 3)

    def test_type(self):
        self.assertRaises(TypeError, fib, "TEST")


class TestFill(unittest.TestCase):
    def test_none(self):
        self.assertIsNotNone(fill([[None, None], [None, None]], 2, 2))


if __name__ == "__main__":
    unittest.main()
