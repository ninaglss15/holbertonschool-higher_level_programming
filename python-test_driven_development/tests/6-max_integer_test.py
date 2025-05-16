#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 2.3]), 2.7)

    def test_negatives(self):
        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 3, 0]), 3)

    def test_strings_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3])

    def test_none_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([None, 2, 3])

if __name__ == "__main__":
    unittest.main()
