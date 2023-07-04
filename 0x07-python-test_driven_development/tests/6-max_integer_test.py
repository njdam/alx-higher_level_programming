#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A test case for unittest for max_integer([..])"""

    def test_ordered_list(self):
        """For testing ordered list to a function."""
        list0 = [0, 1, 2, 3, 4, 5]
        self.assertEqual(max_integer(list0), 5)

    def test_unordered_list(self):
        """For testing unordered list to a function."""
        list1 = [5, 2, 7, 0, 1]
        self.assertEqual(max_integer(list1), 7)

    def test_float_list(self):
        """For testing float numbers in a list to a function."""
        list2 = [9.5, 77.7, 1.0, -100.5, 2.0]
        self.assertEqual(max_integer(list2), 77.7)

    def test_empty_list(self):
        """For testing empty list to a function."""
        list3 = []
        self.assertEqual(max_integer(list3), None)

    def test_single_ellist(self):
        """For testing single element list to a function."""
        list4 = [-7]
        self.assertEqual(max_integer(list4), -7)

    def test_float_int(self):
        """For testing a list with both float and integer to a function."""
        list5 = [2.5, 1, 7, 3.33, 9.0, 4]
        self.assertEqual(max_integer(list5), 9.0)

    def test_string(self):
        """For testing a string to a function."""
        string0 = "Welcome"
        self.assertEqual(max_integer(string0), 'o')

    def test_empty_string(self):
        """For testing empty string to a function."""
        string1 = ""
        self.assertEqual(max_integer(string1), None)

    def test_list_of_string(self):
        """For testing a list of strings to a function."""
        list6 = ["Welcome", "to", "DAM SHOW TV"]
        self.assertEqual(max_integer(list6), 'to')

    def test_strchar(self):
        """For testing a char and a string to a function."""
        list7 = ["CR7", '7']
        self.assertEqual(max_integer(list7), 'CR7')

    def test_numchar(self):
        """For testing a numbers as a char to a function."""
        list8 = ['9', '3', '0', '7', '1']
        self.assertEqual(max_integer(list8), '9')

    def test_char(self):
        """For testing a characters to a function cmp by ascci value."""
        list9 = ['H', 'e', 'l', '0', '7']
        self.assertEqual(max_integer(list9), 'l')


if __name__ == '__main__':
    unittest.main()
