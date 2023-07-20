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

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        r1.update(89, 2)
        r1.update(89, 2, 3)
        r1.update(89, 2, 3, 4)
        r1.update(89, 2, 3, 4, 5)
        expected_r1 = str(f"[Rectangle] ({r1.id}) {r1.x}/{r1.y} - ")
        expected_r1 += str(f"{r1.width}/{r1.height}\n")
        with patch("sys.stdout", new=StringIO()) as output:
            print(r1)
            self.assertEqual(output.getvalue(), expected_r1)

    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        r1.update(width=1, x=2)
        expected_r1 = str(f"[Rectangle] ({r1.id}) {r1.x}/{r1.y} - ")
        expected_r1 += str(f"{r1.width}/{r1.height}\n")
        with patch("sys.stdout", new=StringIO()) as output:
            print(r1)
            self.assertEqual(output.getvalue(), expected_r1)

        r1.update(y=1, width=2, x=3, id=89)
        r1.update(x=1, height=2, y=3, width=4)
        expected_r1 = str(f"[Rectangle] ({r1.id}) {r1.x}/{r1.y} - ")
        expected_r1 += str(f"{r1.width}/{r1.height}\n")
        with patch("sys.stdout", new=StringIO()) as output:
            print(r1)
            self.assertEqual(output.getvalue(), expected_r1)

    def test_print(self):
        r1 = Rectangle(10, 2, 1, 9)
        with patch("sys.stdout", new=StringIO()) as output:
            print(r1)
            expected_r1 = str(f"[Rectangle] ({r1.id}) {r1.x}/{r1.y} - ")
            expected_r1 += str(f"{r1.width}/{r1.height}\n")
            self.assertEqual(output.getvalue(), expected_r1)

    def test_to_dict(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        expected_r1 = "{" + str(f"'x': {r1.x}, 'y': {r1.y}, 'id': {r1.id},")
        expected_r1 += str(f" 'height': {r1.height}, 'width': {r1.width}")
        expected_r1 += "}\n"
        with patch("sys.stdout", new=StringIO()) as output:
            print(r1_dict)
            self.assertEqual(output.getvalue(), expected_r1)

        r2 = Rectangle(1, 1)
        expected_r2 = str(f"[Rectangle] ({r2.id}) {r2.x}/{r2.y} - ")
        expected_r2 += str(f"{r2.width}/{r2.height}\n")
        with patch("sys.stdout", new=StringIO()) as output:
            print(r2)
            self.assertEqual(output.getvalue(), expected_r2)

        with patch("sys.stdout", new=StringIO()) as output:
            r2.update(**r1_dict)
            print(r2)
            expected_u_r2 = str(f"[Rectangle] ({r2.id}) {r2.x}/{r2.y} - ")
            expected_u_r2 += str(f"{r2.width}/{r2.height}\n")
            self.assertEqual(output.getvalue(), expected_u_r2)

        with patch("sys.stdout", new=StringIO()) as output:
            print(r1 == r2)
            self.assertEqual(output.getvalue(), "False\n")


if __name__ == '__main__':
    unittest.main()
