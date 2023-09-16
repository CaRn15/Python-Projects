import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.calculate(1, 1, "+"), 2)

    def test_subtraction(self):
        self.assertEqual(calculator.calculate(4, 2, "-"), 2)
        self.assertEqual(calculator.calculate(2, 4, "-"), -2)

    def test_multiplication(self):
        self.assertEqual(calculator.calculate(2, 5, "*"), 10)

    def test_division(self):
        self.assertEqual(calculator.calculate(4, 2, "/"), 2)
        self.assertEqual(calculator.calculate(0, 4, "/"), "Can't divide by 0!")


if __name__ == "__main__":
    unittest.main()