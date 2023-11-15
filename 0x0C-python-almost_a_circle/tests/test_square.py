#!/usr/bin/python3
"""
    unit test for models/square.py
"""

import unittest
import json
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Defines a TestSquare class """

    def setUp(self):
        self.sq = Square(20)

    def tearDown(self):
        del self.sq

    def test_size(self):
        self.assertEqual(20, self.sq.width)

    def test_x(self):
        self.sq.x = 2
        self.assertEqual(2, self.sq.x)
        self.assertEqual(0, self.sq.y)

    def test_y(self):
        self.sq.y = 2
        self.assertEqual(2, self.sq.y)
        self.assertEqual(0, self.sq.x)

    def test_square_id(self):
        sq1 = Square(1, 0, 0, 12)
        self.assertEqual(12, sq1.id)

    def test_size_str(self):
        with self.assertRaises(TypeError):
            sq1 = Square("s")

    def test_size_list(self):
        with self.assertRaises(TypeError):
            sq1 = Square([1, 2])

    def test_size_bool(self):
        with self.assertRaises(TypeError):
            sq1 = Square(True)

    def test_x_str(self):
        with self.assertRaises(TypeError):
            sq1 = Square(2, "x", 0)

    def test_x_list(self):
        with self.assertRaises(TypeError):
            sq1 = Square(2, [1, 2], 8)

    def test_x_bool(self):
        with self.assertRaises(TypeError):
            sq1 = Square(2, True, 9)

    def test_y_str(self):
        with self.assertRaises(TypeError):
            sq1 = Square(2, 0, "y")

    def test_y_list(self):
        with self.assertRaises(TypeError):
            sq1 = Square(2, 6, [1, 2])

    def test_y_bool(self):
        with self.assertRaises(TypeError):
            sq1 = Square(2, 9, True)

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            sq1 = Square(-2)

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            sq1 = Square(0)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            sq1 = Square(2, -1, 0)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            sq1 = Square(2, 4, -7)

    def test_area(self):
        sq1 = Square(20)
        self.assertEqual(sq1.area(), 20 * 20)

    def test_str_overload(self):
        sq = Square(10, 2, 3, 9)
        self.assertEqual(sq.__str__(), "[Square] (9) 2/3 - 10")

    def test_update(self):
        sq1 = Square(1)
        sq1.update(2, 4)
        self.assertEqual(sq1.__str__(), "[Square] (2) 0/0 - 4")

    def test_update_kwargs(self):
        sq1 = Square(1)
        sq1.update(size=7, y=1, id=12)
        self.assertEqual(sq1.__str__(), "[Square] (12) 0/1 - 7")

    def test_update_both(self):
        sq1 = Square(1)
        sq1.update(2, 4, **{'x': 3, 'y': 4})
        self.assertEqual(sq1.__str__(), "[Square] (2) 0/0 - 4")

    def test_create_dict_equal(self):
        sq1 = Square(1, 3, 5, 6)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertNotEqual(sq1, sq2)

    def test_create_dict_is(self):
        sq1 = Square(1, 3, 5, 6)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertIsNot(sq1, sq2)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            content = json.load(f)
            self.assertEqual(content, [])

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            content = json.load(f)
            self.assertEqual(content, [])

    def test_save_to_file_rect(self):
        Square.save_to_file([Square(1, 3, 4, 5)])
        with open("Square.json", "r") as f:
            content = f.read()
            self.assertEqual(json.loads(content), [{"id": 5,
                                                    "size": 1,
                                                    "x": 3, "y": 4}])

    def test_save_to_file_noargs(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_type(self):
        Square.save_to_file([Square(1, 3, 4, 5)])
        with open("Square.json", "r") as f:
            content = f.read()
            self.assertEqual(str, type(content))

    def test_load_from_file_noexist(self):
        sq1 = Square(1)
        Square.save_to_file([sq1])
        list_output = Square.load_from_file()
        self.assertEqual(sq1.width, list_output[0].size)
