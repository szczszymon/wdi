from zadanie_9 import factorize, print_res
import unittest


class TestFactorize(unittest.TestCase):
    def test_output(self):
        self.output1 = self.prep_output1()
        self.assertIn([1, 1, 2], self.output1)

    @staticmethod
    def prep_output1():
        result = []
        factorize(4, result, [], 0, 1)
        return result


class TestRes(unittest.TestCase):
    def test_result(self):
        self.output2 = self.prep_output2()
        self.assertMultiLineEqual("1 + 1 + 1\n1 + 2\n", print_res(self.output2))

    @staticmethod
    def prep_output2():
        result = []
        factorize(3, result, [], 0, 1)
        return result


if __name__ == "__main__":
    unittest.main()
