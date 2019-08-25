#!/usr/bin/env python

import unittest
import simple_calc

class SimpleCalcTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(simple_calc.add(5, 3), 8)
        self.assertEqual(simple_calc.add(5, -3), 2)
        self.assertEqual(simple_calc.add(-5, -3), -8)

    def test_subtract(self):
        self.assertEqual(simple_calc.subtract(5, 3), 2)
        self.assertEqual(simple_calc.subtract(5, -3), 8)
        self.assertEqual(simple_calc.subtract(-5, -3), -2)

    def test_multiply(self):
        self.assertEqual(simple_calc.multiply(5, 3), 15)
        self.assertEqual(simple_calc.multiply(5, -3), -15)
        self.assertEqual(simple_calc.multiply(-5, -3), 15)

    def test_integer_divide(self):
        self.assertEqual(simple_calc.divide(10, 2), 5)
        self.assertEqual(simple_calc.divide(-12, 3), -4)
        self.assertEqual(simple_calc.divide(12, -4), -3)
        self.assertEqual(simple_calc.divide(-12, -4), 3)

    def test_float_divide(self):
        self.assertEqual(simple_calc.divide(5, 2), 2.5)
        self.assertEqual(simple_calc.divide(-5, 2), -2.5)
        self.assertEqual(simple_calc.divide(5, -2), -2.5)
        self.assertEqual(simple_calc.divide(-5, -2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            simple_calc.divide(0, 0)

        with self.assertRaises(ValueError):
            simple_calc.divide(5, -0)

        with self.assertRaises(ValueError):
            simple_calc.divide(7, -0.0)

if __name__ == '__main__':
    unittest.main()
