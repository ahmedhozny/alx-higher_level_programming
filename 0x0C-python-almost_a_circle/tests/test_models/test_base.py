#!/usr/bin/python3

"""Test cases for Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases"""
    def test_no_id(self):
        inst = Base()
        inst2 = Base()
        self.assertEqual(inst2.id - inst.id, 1)
        inst3 = Base()
        self.assertEqual(inst3.id - inst2.id, 1)

    def test_id_int(self):
        inst = Base(23)
        self.assertEqual(inst.id, 23)

    def test_id_float(self):
        inst = Base(23.1)
        self.assertEqual(inst.id, 23.1)

    def test_id_string(self):
        inst = Base("Base1")
        self.assertEqual(inst.id, "Base1")

    def test_id_none(self):
        inst = Base(None)
        inst2 = Base(None)
        self.assertEqual(inst2.id - inst.id, 1)

    def test_id_optionality(self):
        inst1 = Base()
        inst2 = Base(32)
        inst3 = Base("A")
        inst4 = Base()
        self.assertEqual(inst4.id - inst1.id, 1)
        self.assertEqual(inst2.id, 32)
        self.assertEqual(inst3.id, "A")

    def test_nb_encapsulation(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_to_json_string(self):
        inst = Rectangle(10, 7, 2, 8, id=31)
        dictionary = inst.to_dictionary()
        expected_dict_str = '[{"id": 31, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(Base.to_json_string([dictionary]), expected_dict_str)

    def test_to_json_string_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_none(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_from_json_string(self):
        json_str = ('[{"id": 89, "width": 10, "height": 4},'
                    ' {"id": 7, "width": 1, "height": 7}]')
        list_output = Rectangle.from_json_string(json_str)
        expected_output = [{'id': 89, 'width': 10, 'height': 4},
                           {'id': 7, 'width': 1, 'height': 7}]
        self.assertEqual(list_output, expected_output)

    def test_from_json_string_empty_string(self):
        json_str = ''
        list_output = Rectangle.from_json_string(json_str)
        self.assertEqual(list_output, [])

    def test_from_json_string_none(self):
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_create_rectangle(self):
        inst = Rectangle(3, 5, 1)
        inst2 = Rectangle.create(**inst.to_dictionary())

        self.assertIsInstance(inst2, Rectangle)
        self.assertNotEqual(inst, inst2)
        self.assertEqual(inst.to_dictionary(), inst2.to_dictionary())

    def test_create_square(self):
        inst = Square(4)
        inst2 = Square.create(**inst.to_dictionary())

        self.assertIsInstance(inst2, Square)
        self.assertNotEqual(inst, inst2)
        self.assertEqual(inst.to_dictionary(), inst2.to_dictionary())

    def test_create_unsupported_class(self):
        self.assertIsNone(Base.create())

    def test_load_from_file_nonexistent_file(self):
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output, [])
