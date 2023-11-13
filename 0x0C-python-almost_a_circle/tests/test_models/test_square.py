#!/usr/bin/python3

"""Test cases for Square class"""

import os
from io import StringIO
from contextlib import redirect_stdout
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases"""
    def setUp(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def tearDown(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout.

        Args:
            sq (Square): The Square to print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = StringIO()
        with redirect_stdout(capture):
            if method == "print":
                print(sq)
            elif method == "display":
                sq.display()
        return capture

    def test_square_no_parameters(self):
        self.assertRaises(TypeError, Square)

    def test_square_no_id(self):
        inst1 = Square(1)
        inst2 = Square(1)
        inst3 = Square(3, 4, 1)
        self.assertEqual(inst1.id, inst2.id - 1)
        self.assertEqual(inst2.id, inst3.id - 1)

    def test_square_same_id(self):
        inst1 = Square(1, 2, id=1)
        inst2 = Square(1, 2, id=1)
        self.assertEqual(inst1.id, inst2.id)

    def test_size_type(self):
        self.assertRaises(TypeError, Rectangle, 32.1)

    def test_size_type2(self):
        self.assertRaises(TypeError, Rectangle, None)

    def test_size_value(self):
        inst = Square(4)
        self.assertEqual(inst.size, 4)

    def test_size_value2(self):
        inst = Square(5)
        self.assertEqual(inst.size, inst.width)
        self.assertEqual(inst.size, inst.height)

    def test_area_type(self):
        inst = Square(3)
        self.assertIsInstance(inst.area(), int)

    def test_area(self):
        inst = Square(5)
        self.assertEqual(inst.area(), 25)

    def test_area2(self):
        inst = Square(5)
        self.assertEqual(inst.area(), inst.size ** 2)

    def test_area3(self):
        inst = Square(5)
        self.assertEqual(inst.area(), inst.width * inst.height)

    def test_area4(self):
        inst1 = Square(5)
        inst2 = Rectangle(5, 5)
        self.assertEqual(inst1.area(), inst2.area())

    def test_display(self):
        inst = Square(4)
        capture = TestSquare.capture_stdout(inst, "display")
        self.assertEqual(capture.getvalue(), "####\n####\n####\n####\n")

    def test_display2(self):
        inst = Square(4, 1)
        capture = TestSquare.capture_stdout(inst, "display")
        self.assertEqual(capture.getvalue(), " ####\n ####\n ####\n ####\n")

    def test_display3(self):
        inst = Square(4, y=2)
        capture = TestSquare.capture_stdout(inst, "display")
        self.assertEqual(capture.getvalue(), "\n\n####\n####\n####\n####\n")

    def test_display4(self):
        inst = Square(2, 1, 2)
        capture = TestSquare.capture_stdout(inst, "display")
        self.assertEqual(capture.getvalue(), "\n\n ##\n ##\n")

    def test_rectangle_print(self):
        inst = Square(4, 6, 2, 12)
        capture = TestSquare.capture_stdout(inst, "print")
        self.assertEqual(capture.getvalue(), "[Square] (12) 6/2 - 4\n")

    def test_rectangle_print2(self):
        inst = Square(5, 5, 1)
        capture = TestSquare.capture_stdout(inst, "print")
        self.assertEqual(capture.getvalue(), "[Square] ({}) 5/1 - 5\n".format(inst.id))

    def test_update(self):
        inst1 = Square(3, id="A")
        inst1.update(None)
        inst2 = Square(3)
        self.assertEqual(inst1.id, inst2.id - 1)

    def test_update2(self):
        inst = Square(32)
        inst.update(31, 10)
        self.assertEqual(inst.id, 31)

    def test_update3(self):
        inst = Square(32)
        inst.update(1, 3, 3)
        self.assertEqual(inst.size, 3)

    def test_update4(self):
        inst = Square(32, 10)
        inst.update(1, 3, 3, 2)
        self.assertEqual((inst.x, inst.y), (3, 2))

    def test_update5(self):
        inst = Square(32, 10, y=1)
        inst.update(1, 3, 3, 2)
        self.assertEqual((inst.x, inst.y), (3, 2))

    def test_update6(self):
        inst = Square(32, 10, 3)
        inst.update(**{"id": 52, "size": 4})
        self.assertEqual(inst.id, 52)
        self.assertEqual(inst.size, 4)
        self.assertEqual(inst.x, 10)
        self.assertEqual(inst.y, 3)

    def test_update7(self):
        inst = Square(32, 10, 1)
        inst.update(3, 2, **{"id": 52, "size": 4, "x": 2})
        self.assertEqual(inst.id, 3)
        self.assertEqual(inst.size, 2)
        self.assertEqual(inst.x, 10)
        self.assertEqual(inst.y, 1)

    def test_update8(self):
        inst = Square(32, 1, 4)
        inst.update(**{"id": 52, "size": 4, "x": 1, "y": 2})
        self.assertEqual(inst.id, 52)
        self.assertEqual(inst.size, 4)
        self.assertEqual(inst.x, 1)
        self.assertEqual(inst.y, 2)

    def test_update_empty(self):
        inst = Square(32, 10, 1, 21)
        inst.update()
        self.assertEqual(inst.id, 21)
        self.assertEqual(inst.size, 32)
        self.assertEqual(inst.x, 10)
        self.assertEqual(inst.y, 1)

    def test_to_dictionary(self):
        inst = Square(3, 4, 5, 6)
        dict_a = {"id": 6, "size": 3, "x": 4, "y": 5}
        self.assertEqual(inst.to_dictionary(), dict_a)

    def test_update_and_to_dictionary(self):
        inst = Square(1, 2, 3, 4)
        dict_a = {"id": 4, "size": 1, "x": 2, "y": 3}
        inst.update(**dict_a)
        self.assertEqual(inst.to_dictionary(), dict_a)

    def test_update_and_to_dictionary2(self):
        inst = Square(1, 2, 3, 4)
        dict_a = {"id": 7, "size": 3, "x": 5, "y": 6}
        inst.update(7, 3, 5, 6)
        self.assertEqual(inst.to_dictionary(), dict_a)

    def test_save_to_file(self):
        inst1 = Square(10, 7, 2, 8)
        inst2 = Square(2, 4, id=4)
        Square.save_to_file([inst1, inst2])

        with open("Square.json", "r") as file:
            content = file.read()
            expected_content = ('[{"id": 8, "size": 10, "x": 7, "y": 2},'
                                ' {"id": 4, "size": 2, "x": 4, "y": 0}]')
            self.assertEqual(content, expected_content)

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_filename(self):
        r1 = Square(10, 7, 2)
        Square.save_to_file([r1])
        self.assertTrue(os.path.exists("Square.json"))

    def test_load_from_file(self):
        inst1 = Square(23, 1, 4)
        inst2 = Square(2, 4, 1)
        list_input = [inst1, inst2]

        Square.save_to_file(list_input)
        list_output = Square.load_from_file()

        self.assertIsInstance(list_output, list)
        self.assertEqual(len(list_output), 2)
        self.assertNotEqual(list_input[0], list_output[0])
        self.assertEqual(list_input[0].to_dictionary(), list_output[0].to_dictionary())
