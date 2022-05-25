#Problem 1

import unittest
import Calculator1

class TestProblem1(unittest. TestCase):
    def test_add(self):
        self.assertEqual(12,Calculator1.Calculator().add(5,7))
    def test_sub(self):
        self.assertEqual(1,Calculator1.Calculator().sub(5,4))
    def test_mul(self):
        self.assertEqual(25,Calculator1.Calculator().mul(5,5))
    def test_div(self):
        self.assertEqual(3.0,Calculator1.Calculator().div(12,4))

if __name__ == "__main__":
    unittest.main()

#Problem 2

''' import unittest

def factorial(n=0):
    fact = 1;
    if (n!=0):
        for i in range(n):
            fact *= n
            n = n-1
    return fact;

class TestFactorial(unittest.TestCase):
    def test_zero_factorial_is_one(self):
        self.assertEqual(1,factorial(0))
    def test_one_factorial_is_one(self):
        self.assertEqual(1,factorial(1))
    def test_five_factorial_is_120(self):
        self.assertEqual(120,factorial(5))

if __name__ == "__main__":
    unittest.main() '''