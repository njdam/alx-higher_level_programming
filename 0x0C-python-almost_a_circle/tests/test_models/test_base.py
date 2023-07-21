#!/usr/bin/python3
"""Unit Test Cases for base.py file."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch
import os


class TestClassBase(unittest.TestCase):
    """A test cases for class Base."""

    def test_init_0with_id(self):
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_init_1without_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)
        self.assertEqual(base2.id, base1.id + 1)

    def test_init_2with_None(self):
        base3 = Base(None)
        base4 = Base()
        self.assertEqual(base3.id, base4.id - 1)

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
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b1.id + 1)
        self.assertEqual(b3.id, b2.id + 1)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, b3.id + 1)
        self.assertEqual(b1.id, b5.id - 3)

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

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        with patch("sys.stdout", new=StringIO()) as output:
            print(r1)
            expected = str(f"[Rectangle] ({r1.id}) {r1.x}/{r1.y} - ")
            expected += str(f"{r1.width}/{r1.height}\n")
            self.assertEqual(output.getvalue(), expected)

        with patch("sys.stdout", new=StringIO()) as output:
            print(r2)
            expected2 = str(f"[Rectangle] ({r2.id}) {r2.x}/{r2.y} - ")
            expected2 += str(f"{r2.width}/{r2.height}\n")
            self.assertEqual(output.getvalue(), expected2)

        with patch("sys.stdout", new=StringIO()) as output:
            print(r1 is r2)
            self.assertEqual(output.getvalue(), "False\n")

        with patch("sys.stdout", new=StringIO()) as output:
            print(r1 == r2)
            self.assertEqual(output.getvalue(), "False\n")

    def test_load_from_rfile(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        with patch("sys.stdout", new=StringIO()) as output:
            expected = str(f"[{id(r1)}] [Rectangle] ({r1.id}) 2/8 - 10/7\n")
            expected += str(f"[{id(r2)}] [Rectangle] ({r2.id}) 0/0 - 2/4\n")
            for rect in list_rectangles_input:
                print("[{}] {}".format(id(rect), rect))
            self.assertEqual(output.getvalue(), expected)

        with patch("sys.stdout", new=StringIO()) as output:
            ids = []
            for rect in list_rectangles_output:
                print("[{}] {}".format(id(rect), rect))
                ids.append(id(rect))
            expecte2 = str(f"[{ids[0]}] [Rectangle] ({r1.id}) 2/8 - 10/7\n")
            expecte2 += str(f"[{ids[1]}] [Rectangle] ({r2.id}) 0/0 - 2/4\n")
            self.assertEqual(output.getvalue(), expecte2)

    def test_load_from_sfile(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        with patch("sys.stdout", new=StringIO()) as output:
            expected3 = str(f"[{id(s1)}] [Square] ({s1.id}) 0/0 - 5\n")
            expected3 += str(f"[{id(s2)}] [Square] ({s2.id}) 9/1 - 7\n")
            for square in list_squares_input:
                print("[{}] {}".format(id(square), square))
            self.assertEqual(output.getvalue(), expected3)

        with patch("sys.stdout", new=StringIO()) as output:
            ids = []
            for square in list_squares_output:
                print("[{}] {}".format(id(square), square))
                ids.append(id(square))
            expected4 = str(f"[{ids[0]}] [Square] ({s1.id}) 0/0 - 5\n")
            expected4 += str(f"[{ids[1]}] [Square] ({s2.id}) 9/1 - 7\n")
            self.assertEqual(output.getvalue(), expected4)

class TestBase_save_to_file_csv(unittest.TestCase):
    """Test cases for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """For deleting any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rect(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rect(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_sq(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_sq(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_files__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrites(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_files__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_lists(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_arg_s(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg_s(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Test cases for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """for deletion of any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rect(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rect(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rect_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_sq(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_sq(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_sq_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_files(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_argi(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == '__main__':
    unittest.main()
