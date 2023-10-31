#!/usr/bin/python3

""" Prints any size of a square"""


def print_square(size):
    """
    prints a square of a given size

    Args:
        size (int): length of one side of a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
