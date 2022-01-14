from laboratorium_8.zadanie_8 import check_parentheses, drop_different, UnevenNoOfParentheses
import unittest


class TestParentheses(unittest.TestCase):
    def test_except(self):
        self.assertTrue(check_parentheses("()(((()))()"))
        self.assertFalse(check_parentheses("()()"))


class TestDrop(unittest.TestCase):
    def test_different(self):
        self.assertNotIn("test", drop_different("()(test)()"))


if __name__ == "__main__":
    unittest.main()
