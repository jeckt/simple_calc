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
        self.assertEqual(simple_calc.multiply(5, 3), 2)
        self.assertEqual(simple_calc.multiply(5, -3), 8)
        self.assertEqual(simple_calc.multiply(-5, -3), -2)

if __name__ == '__main__':
    unittest.main()
