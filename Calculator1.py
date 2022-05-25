#Calculator

class Calculator():
    def add(self, x,y):
        ret = x+y
        return ret
    def sub(self, x,y):
        ret = x-y
        return ret
    def mul(self, x,y):
        ret = x * y
        return ret
    def div(self, x,y):
        ret = x / y
        return ret

import unittest

class TestProblem1(unittest. TestCase):
    def test_add(self):
        self.assertEqual(12,Calculator().add(5,7))
    def test_sub(self):
        self.assertEqual(1,Calculator().sub(5,4))
    def test_mul(self):
        self.assertEqual(25,Calculator().mul(5,5))
    def test_div(self):
        self.assertEqual(3.0,Calculator().div(12,4))

if __name__ == "__main__":
    unittest.main()