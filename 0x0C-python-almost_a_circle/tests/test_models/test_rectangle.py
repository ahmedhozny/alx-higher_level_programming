#!/usr/bin/python3

"""Test cases for Rectangle class"""

import os
from io import StringIO
from contextlib import redirect_stdout
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases"""
    def setUp(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def tearDown(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = StringIO()
        with redirect_stdout(capture):
            if method == "print":
                print(rect)
            elif method == "display":
                rect.display()
        return capture

    def test_rectangle_no_parameters(self):
        self.assertRaises(TypeError, Rectangle)

    def test_rectangle_missing_parameters(self):
        self.assertRaises(TypeError, Rectangle, 1)

    def test_rectangle_no_id(self):
        inst1 = Rectangle(1, 2)
        inst2 = Rectangle(1, 2)
        inst3 = Rectangle(3, 4, 1, 3)
        self.assertEqual(inst1.id, inst2.id - 1)
        self.assertEqual(inst2.id, inst3.id - 1)

    def test_rectangle_same_id(self):
        inst1 = Rectangle(1, 2, id=1)
        inst2 = Rectangle(1, 2, id=1)
        self.assertEqual(inst1.id, inst2.id)

    def test_same_parent_id(self):
        inst1 = Rectangle(1, 2, id=134)
        inst2 = Base(134)
        self.assertIsNot(inst1, inst2)

    def test_rectangle_width(self):
        inst1 = Rectangle(4, 3)
        self.assertEqual(inst1.width, 4)

    def test_rectangle_height(self):
        inst1 = Rectangle(6, 3)
        self.assertEqual(inst1.height, 3)

    def test_width_type(self):
        self.assertRaises(TypeError, Rectangle, 32.0, 3)

    def test_width_type2(self):
        self.assertRaises(TypeError, Rectangle, "ABC", 12)

    def test_height_type(self):
        self.assertRaises(TypeError, Rectangle, 12, 32.0)

    def test_height_type2(self):
        self.assertRaises(TypeError, Rectangle, 2, "DEAF")

    def test_width_value(self):
        self.assertRaises(ValueError, Rectangle, -12, 13)

    def test_width_value2(self):
        self.assertRaises(ValueError, Rectangle, 0, 13)

    def test_height_value(self):
        self.assertRaises(ValueError, Rectangle, 1, -13)

    def test_height_value2(self):
        self.assertRaises(ValueError, Rectangle, 1, 0)

    def test_x_type(self):
        self.assertRaises(TypeError, Rectangle, 1, 3, "-1")

    def test_x_type2(self):
        self.assertRaises(TypeError, Rectangle, 1, 3, -12.0, 1)

    def test_y_type(self):
        self.assertRaises(TypeError, Rectangle, 1, 3, 1, "LOL")

    def test_y_type2(self):
        self.assertRaises(TypeError, Rectangle, 1, 3, 12, 132.0)

    def test_area_type(self):
        inst = Rectangle(3, 6)
        self.assertIsInstance(inst.area(), int)

    def test_area_value(self):
        inst = Rectangle(3, 6, 1, 5)
        self.assertEqual(inst.area(), 18)

    def test_display(self):
        inst = Rectangle(4, 6)
        capture = TestRectangle.capture_stdout(inst, "display")
        self.assertEqual(capture.getvalue(), "####\n####\n####\n####\n####\n####\n")

    def test_display2(self):
        inst = Rectangle(2, 2)
        capture = TestRectangle.capture_stdout(inst, "display")
        self.assertEqual(capture.getvalue(), "##\n##\n")

    def test_display3(self):
        inst = Rectangle(3, 2, 3, 0)
        capture = TestRectangle.capture_stdout(inst, "display")
        self.assertEqual(capture.getvalue(), "   ###\n   ###\n")

    def test_display4(self):
        inst = Rectangle(3, 2, 0, 2)
        capture = TestRectangle.capture_stdout(inst, "display")
        self.assertEqual(capture.getvalue(), "\n\n###\n###\n")

    def test_display5(self):
        inst = Rectangle(3, 2, 2, 2)
        capture = TestRectangle.capture_stdout(inst, "display")
        self.assertEqual(capture.getvalue(), "\n\n  ###\n  ###\n")

    def test_rectangle_print(self):
        inst = Rectangle(4, 6, 2, 1, 12)
        capture = TestRectangle.capture_stdout(inst, "print")
        self.assertEqual(capture.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")

    def test_rectangle_print2(self):
        inst = Rectangle(5, 5, 1)
        capture = TestRectangle.capture_stdout(inst, "print")
        self.assertEqual(capture.getvalue(), "[Rectangle] ({}) 1/0 - 5/5\n".format(inst.id))

    def test_update(self):
        inst1 = Rectangle(3, 2, id="A")
        inst1.update(None)
        inst2 = Rectangle(3, 2)
        self.assertEqual(inst1.id, inst2.id - 1)

    def test_update2(self):
        inst = Rectangle(32, 10)
        inst.update(1, 10)
        self.assertEqual((inst.width, inst.height), (10, 10))

    def test_update3(self):
        inst = Rectangle(32, 10)
        inst.update(1, 3, 3)
        self.assertEqual((inst.width, inst.height), (3, 3))

    def test_update4(self):
        inst = Rectangle(32, 10)
        inst.update(1, 3, 3, 2)
        self.assertEqual((inst.x, inst.y), (2, 0))

    def test_update5(self):
        inst = Rectangle(32, 10, x=3, y=1)
        inst.update(1, 3, 3, 2, 4)
        self.assertEqual((inst.x, inst.y), (2, 4))

    def test_update6(self):
        inst = Rectangle(32, 10, x=3, y=1)
        inst.update(**{"id": 52, "width": 4})
        self.assertEqual(inst.id, 52)
        self.assertEqual(inst.width, 4)
        self.assertEqual(inst.height, 10)
        self.assertEqual(inst.x, 3)
        self.assertEqual(inst.y, 1)

    def test_update7(self):
        inst = Rectangle(32, 10, x=3, y=1)
        inst.update(3, 2, **{"id": 52, "width": 4, "height": 43})
        self.assertEqual(inst.id, 3)
        self.assertEqual(inst.width, 2)
        self.assertEqual(inst.height, 10)
        self.assertEqual(inst.x, 3)
        self.assertEqual(inst.y, 1)

    def test_update8(self):
        inst = Rectangle(32, 10, x=3, y=1)
        inst.update(**{"id": 52, "width": 4, "height": 3, "x": 1, "y": 2})
        self.assertEqual(inst.id, 52)
        self.assertEqual(inst.width, 4)
        self.assertEqual(inst.height, 3)
        self.assertEqual(inst.x, 1)
        self.assertEqual(inst.y, 2)

    def test_update_empty(self):
        inst = Rectangle(32, 10, x=3, y=1, id=21)
        inst.update()
        self.assertEqual(inst.id, 21)
        self.assertEqual(inst.width, 32)
        self.assertEqual(inst.height, 10)
        self.assertEqual(inst.x, 3)
        self.assertEqual(inst.y, 1)

    def test_to_dictionary(self):
        inst = Rectangle(3, 4, 5, 6, 7)
        dict_a = {"id": 7, "width": 3, "height": 4, "x": 5, "y": 6}
        self.assertEqual(inst.to_dictionary(), dict_a)

    def test_update_and_to_dictionary(self):
        inst = Rectangle(1, 2, 3, 4, 5)
        dict_a = {"id": 7, "width": 3, "height": 4, "x": 5, "y": 6}
        inst.update(**dict_a)
        self.assertEqual(inst.to_dictionary(), dict_a)

    def test_update_and_to_dictionary2(self):
        inst = Rectangle(1, 2, 3, 4, 5)
        dict_a = {"id": 7, "width": 3, "height": 4, "x": 5, "y": 6}
        inst.update(7, 3, 4, 5, 6)
        self.assertEqual(inst.to_dictionary(), dict_a)

    def test_save_to_file(self):
        inst1 = Rectangle(10, 7, 2, 8, 3)
        inst2 = Rectangle(2, 4, id=4)
        Rectangle.save_to_file([inst1, inst2])

        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected_content = ('[{"id": 3, "width": 10, "height": 7, "x": 2, "y": 8},'
                                ' {"id": 4, "width": 2, "height": 4, "x": 0, "y": 0}]')
            self.assertEqual(content, expected_content)

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_filename(self):
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_load_from_file(self):
        inst1 = Rectangle(10, 7, 2, 8)
        inst2 = Rectangle(2, 4)
        list_input = [inst1, inst2]

        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()

        self.assertIsInstance(list_output, list)
        self.assertEqual(len(list_output), 2)
        self.assertNotEqual(list_input[0], list_output[0])
        self.assertEqual(list_input[0].to_dictionary(),
                         list_output[0].to_dictionary())
