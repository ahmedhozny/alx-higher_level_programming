#!/usr/bin/python3

"""Defines a Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method that returns area of a square"""
        return self.__size * self.__size

    def __str__(self):
        """Method that returns a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
