#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
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
        self.assertEqual(max_integer([7]), 7)

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_duplicates(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_string_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

if __name__ == '__main__':
    unittest.main()
