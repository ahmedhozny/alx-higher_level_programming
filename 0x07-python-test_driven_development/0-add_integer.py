#!/usr/bin/python3

"""A module for adding numbers."""


def add_integer(a, b=98):
    """
        Adds two integers.

        Args:
            a (int or float): The first integer or float.
            b (int or float): The second integer or float, defaults to 98.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
