#!/usr/bin/python3
"""A Test Case file to test rectangle.py file by unittest Test Cases."""

import unittest
from unittest.mock import patch

from io import StringIO

from models.square import Square
from models.rectangle import Rectangle


class TestingClassSquare(unittest.TestCase):
    """A test cases for testing a square inherited from Rectangle class."""

    def test_square_if_is_rectangle(self):
        self.assertIsInstance(Square(5), Rectangle)

    def test_width_height_only(self):
        r1 = Square(10)
        r2 = Square(2)
        self.assertEqual(r2.id, r1.id + 1)

    def test_with_all_args(self):
        r3 = Square(10, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test__type_error(self):
        with self.assertRaises(TypeError):
            Square("10")
            Square(2, 0, "0")

    def test_neg_value(self):
        with self.assertRaises(ValueError):
            Square(10, -2, 3)
            Square(10, 2, {})
            Square(-10, 2)

    def test_set_size(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_area_rectangle(self):
        r1 = Square(3)
        r2 = Square(2)
        r3 = Square(8, 0, 0, 12)
        self.assertEqual(r1.area(), 9)
        self.assertEqual(r2.area(), 4)
        self.assertEqual(r3.area(), 64)

    def test_display_rectangle(self):
        r1 = Square(4)
        expected_output = "####\n####\n####\n####\n"
        with patch("sys.stdout", new=StringIO()) as output:
            r1.display()
            self.assertEqual(output.getvalue(), expected_output)

        r2 = Square(2)
        expected_output = "##\n##\n"
        with patch("sys.stdout", new=StringIO()) as output:
            r2.display()
            self.assertEqual(output.getvalue(), expected_output)

        r3 = Square(3, 2, 2)
        expected_r3 = "\n\n  ###\n  ###\n  ###\n"
        with patch("sys.stdout", new=StringIO()) as output:
            r3.display()
            self.assertEqual(output.getvalue(), expected_r3)

        r4 = Square(2, 1, 0)
        expected_r4 = " ##\n ##\n"
        with patch("sys.stdout", new=StringIO()) as output:
            r4.display()
            self.assertEqual(output.getvalue(), expected_r4)

    def test_str_repr(self):
        r1 = Square(4, 2, 1, 12)
        expected_r1 = "[Square] (12) 2/1 - 4\n"
        with patch("sys.stdout", new=StringIO()) as output:
            print(r1)
            self.assertEqual(output.getvalue(), expected_r1)

        r2 = Square(5, 1, 0)
        r3 = Square(5, 1)
        expected_r3 = f"[Square] ({r2.id + 1}) 1/0 - 5\n"
        with patch("sys.stdout", new=StringIO()) as output:
            print(r3)
            self.assertEqual(output.getvalue(), expected_r3)

    def test_update(self):
        r1 = Square(10, 10, 10)
        r1.update(89)
        r1.update(89, 2)
        r1.update(89, 2, 3)
        r1.update(89, 2, 3, 4)
        r1.update(89, 2, 3, 4, 5)
        expected_r1 = str(f"[Square] ({r1.id}) {r1.x}/{r1.y} - ")
        expected_r1 += str(f"{r1.size}\n")
        with patch("sys.stdout", new=StringIO()) as output:
            print(r1)
            self.assertEqual(output.getvalue(), expected_r1)

    def test_update_kwargs(self):
        r1 = Square(10, 10, 10, 10)
        r1.update(height=1)
        r1.update(width=1, x=2)
        expected_r1 = str(f"[Square] ({r1.id}) {r1.x}/{r1.y} - ")
        expected_r1 += str(f"{r1.size}\n")
        with patch("sys.stdout", new=StringIO()) as output:
            print(r1)
            self.assertEqual(output.getvalue(), expected_r1)

        r1.update(y=1, x=3, id=89)
        r1.update(x=1, size=4, y=3, id=4)
        expected_r1 = str(f"[Square] ({r1.id}) {r1.x}/{r1.y} - ")
        expected_r1 += str(f"{r1.size}\n")
        with patch("sys.stdout", new=StringIO()) as output:
            print(r1)
            self.assertEqual(output.getvalue(), expected_r1)

    def test_to_dict(self):
        r1 = Square(10, 2, 1)
        r1_dict = r1.to_dictionary()
        exp_dict_r1 = {'id': r1.id, 'x': r1.x, 'size': r1.size, 'y': r1.y}
        expected_r1 = str(exp_dict_r1) + "\n"
        with patch("sys.stdout", new=StringIO()) as output:
            print(r1_dict)
            self.assertEqual(output.getvalue(), expected_r1)

        r2 = Square(1, 1)
        expected_r2 = str(f"[Square] ({r2.id}) {r2.x}/{r2.y} - ")
        expected_r2 += str(f"{r2.size}\n")
        with patch("sys.stdout", new=StringIO()) as output:
            print(r2)
            self.assertEqual(output.getvalue(), expected_r2)

        with patch("sys.stdout", new=StringIO()) as output:
            r2.update(**r1_dict)
            print(r2)
            expected_u_r2 = str(f"[Square] ({r2.id}) {r2.x}/{r2.y} - ")
            expected_u_r2 += str(f"{r1.size}\n")
            self.assertEqual(output.getvalue(), expected_u_r2)

        with patch("sys.stdout", new=StringIO()) as output:
            print(r1 == r2)
            self.assertEqual(output.getvalue(), "False\n")


if __name__ == '__main__':
    unittest.main()
