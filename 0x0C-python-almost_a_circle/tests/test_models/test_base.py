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

    def test_json_string_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        expected_f = "[{" + str(f'"x": {r1.x}, "y": {r1.y}, "id": {r1.id}')
        expected_f += str(f', "height": {r1.height}, "width": {r1.width}')
        expected_f += '}, {' + str(f'"x": {r2.x}, "y": {r2.y}, "id": {r2.id}')
        expected_f += str(f', "height": {r2.height}, "width": {r2.width}')
        expected_f += "}]\n"
        with patch("sys.stdout", new=StringIO()) as output:
            with open("Rectangle.json", "r") as file:
                print(file.read())
            self.assertEqual(output.getvalue(), expected_f)

    def test_json_string_return(self):
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        expected_inp = str("[<class 'list'>] [{'id': 89, 'width': 10, ")
        expected_inp += str("'height': 4}, {'id': 7, 'width': 1, ")
        expected_inp += str("'height': 7}]\n")
        with patch("sys.stdout", new=StringIO()) as output:
            print("[{}] {}".format(type(list_input), list_input))
            self.assertEqual(output.getvalue(), expected_inp)

        expected_jsl = "[<class 'str'>] " + '[{"id": 89, "width": 10, '
        expected_jsl += str('"height": 4}, {"id": 7, "width": 1, ')
        expected_jsl += str('"height": 7}]\n')
        with patch("sys.stdout", new=StringIO()) as output:
            print("[{}] {}".format(type(json_list_input), json_list_input))
            self.assertEqual(output.getvalue(), expected_jsl)

        expected_outp = str("[<class 'list'>] [{'id': 89, 'width': 10, ")
        expected_outp += str("'height': 4}, {'id': 7, 'width': 1, ")
        expected_outp += str("'height': 7}]\n")
        with patch("sys.stdout", new=StringIO()) as output:
            print("[{}] {}".format(type(list_output), list_output))
            self.assertEqual(output.getvalue(), expected_outp)


if __name__ == '__main__':
    unittest.main()
