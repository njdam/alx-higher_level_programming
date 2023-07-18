#!/usr/bin/python3
"""A Test Case file to test rectangle.py file by unittest Test Cases."""

import unittest
from unittest.mock import patch

from io import StringIO

from models.base import Base
from models.rectangle import Rectangle


class TestingClassRectangle(unittest.TestCase):
    """A test cases for testing a rectangle inherited from Base class."""

    def test_rectangle_if_is_base(self):
        self.assertIsInstance(Rectangle(5, 7), Base)

    def test_width_height_only(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, r1.id + 1)

    def test_with_all_args(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test__type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
            Rectangle("6", 7)

    def test_neg_value(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)
            Rectangle(10, 2, {}, 0)
            Rectangle(10, -2)
            Rectangle(-10, 2)

    def test_area_rectangle(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display_rectangle(self):
        r1 = Rectangle(4, 6)
        expected_output = "####\n####\n####\n####\n####\n####\n"
        with patch("sys.stdout", new=StringIO()) as output:
            r1.display()
            self.assertEqual(output.getvalue(), expected_output)

        r2 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch("sys.stdout", new=StringIO()) as output:
            r2.display()
            self.assertEqual(output.getvalue(), expected_output)

        r3 = Rectangle(2, 3, 2, 2)
        expected_r3 = "\n\n  ##\n  ##\n  ##\n"
        with patch("sys.stdout", new=StringIO()) as output:
            r3.display()
            self.assertEqual(output.getvalue(), expected_r3)

        r4 = Rectangle(3, 2, 1, 0)
        expected_r4 = " ###\n ###\n"
        with patch("sys.stdout", new=StringIO()) as output:
            r4.display()
            self.assertEqual(output.getvalue(), expected_r4)

    def test_str_repr(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_r1 = "[Rectangle] (12) 2/1 - 4/6\n"
        with patch("sys.stdout", new=StringIO()) as output:
            print(r1)
            self.assertEqual(output.getvalue(), expected_r1)

        r2 = Rectangle(5, 5, 1, 0)
        r3 = Rectangle(5, 5, 1)
        expected_r3 = f"[Rectangle] ({r2.id + 1}) 1/0 - 5/5\n"
        with patch("sys.stdout", new=StringIO()) as output:
            print(r3)
            self.assertEqual(output.getvalue(), expected_r3)


if __name__ == '__main__':
    unittest.main()
