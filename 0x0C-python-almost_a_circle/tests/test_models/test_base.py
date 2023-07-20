#!/usr/bin/python3
"""Unit Test Cases for base.py file."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestClassBase(unittest.TestCase):
    """A test cases for class Base."""

    def test_init_0with_id(self):
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_init_1without_id(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)

    def test_init_2with_None(self):
        base3 = Base(None)
        self.assertEqual(base3.id, 3)

    def test_init_3with_non_id(self):
        base4 = Base("7")
        base5 = Base(5 + 2)
        self.assertEqual(base4.id, "7")
        self.assertEqual(base5.id, 7)

    def test_init_4with_main_ex(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 4)
        self.assertEqual(b2.id, 5)
        self.assertEqual(b3.id, 6)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 7)
        self.assertEqual(b1.id, 4)

    def test_json_dict(self):
        r1 = Rectangle(10, 7, 2, 8)
        r1_dict = r1.to_dictionary()
        expected_r1 = "{" + str(f"'x': {r1.x}, 'y': {r1.y}, 'id': {r1.id},")
        expected_r1 += str(f" 'height': {r1.height}, 'width': {r1.width}")
        expected_r1 += "}\n"
        with patch("sys.stdout", new=StringIO()) as output:
            print(r1_dict)
            self.assertEqual(output.getvalue(), expected_r1)

        expected_r2 = "[{" + str(f'"x": {r1.x}, "y": {r1.y}, "id": {r1.id}')
        expected_r2 += str(f', "height": {r1.height}, "width": {r1.width}')
        expected_r2 += "}]\n"
        with patch("sys.stdout", new=StringIO()) as output:
            json_dic_r1 = Base.to_json_string([r1_dict])
            print(json_dic_r1)
            self.assertEqual(output.getvalue(), expected_r2)


if __name__ == '__main__':
    unittest.main()
