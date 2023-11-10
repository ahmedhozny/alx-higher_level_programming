#!/usr/bin/python3

"""Tests max_integer function"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class TestIntegerMax(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def testValue(self):
        """Some tests on values"""
        self.assertEquals(max_integer([1, 2, 3, 4]), 4)
        self.assertEquals(max_integer([]), None)
        self.assertEquals(max_integer([21, 10, 123, 31, 32]), 123)
        self.assertEquals(max_integer("ABCDEFG"), "G")
