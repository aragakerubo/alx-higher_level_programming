#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This class contains the tests for the max_integer function.
    """

    def test_ordered_list(self):
        """
        Test max_integer with an ordered list.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """
        Test max_integer with an unordered list.
        """
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """
        Test max_integer with an empty list.
        """
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """
        Test max_integer with a list with only one element.
        """
        self.assertEqual(max_integer([1]), 1)

    def test_max_at_beginning(self):
        """
        Test max_integer with the max number at the beginning of the list.
        """
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_max_at_end(self):
        """
        Test max_integer with the max number at the end of the list.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer(self):
        """
        Test max_integer with a list of integers.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_float(self):
        """
        Test max_integer with a list of floats.
        """
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_max_string(self):
        """
        Test max_integer with a list of strings.
        """
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")

    def test_max_string_empty(self):
        """
        Test max_integer with an empty string.
        """
        self.assertEqual(max_integer(""), None)

    def test_max_string_int(self):
        """
        Test max_integer with a list of strings and integers.
        """
        self.assertEqual(max_integer(["a", 2, "c", 4]), 4)

    def test_max_string_float(self):
        """
        Test max_integer with a list of strings and floats.
        """
        self.assertEqual(max_integer(["a", 2.2, "c", 4.4]), 4.4)

    def test_max_string_int_float(self):
        """
        Test max_integer with a list of strings, integers, and floats.
        """
        self.assertEqual(max_integer(["a", 2, "c", 4.4]), 4.4)

    def test_max_integer_negative(self):
        """
        Test max_integer with a list of negative integers.
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_negative_float(self):
        """
        Test max_integer with a list of negative floats.
        """
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -4.4]), -1.1)


if __name__ == "__main__":
    unittest.main()
