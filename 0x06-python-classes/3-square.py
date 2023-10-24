#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """
        Initializes a square with a specified size.
        Args:
            size (int): The length of one side of the square. Defaults to 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.
        Returns:
            int: The area of the square, which is the size squared.
        """
        return self.__size * self.__size
