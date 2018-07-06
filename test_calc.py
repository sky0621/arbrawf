import unittest

import calc

class TestCalc(unittest.TestCase):

    def test_divide_normal(self):
        self.assertEqual(calc.divide(2, 2), 1)

    def test_divide_contain_zero(self):
        self.assertEqual(calc.divide(0, 1), 0)
