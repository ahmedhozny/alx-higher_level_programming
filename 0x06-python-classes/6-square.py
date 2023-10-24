#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a specified size.
        Args:
            size (int): The length of one side of the square. Defaults to 0.
            position (tuple): The position on x and y coordinates.
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculate and return the area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Print a square of '#' characters to the standard output.
        """
        import sys
        if self.size == 0:
            sys.stdout.write("\n")
        else:
            for i in range(self.position[1]):
                sys.stdout.write("\n")
            for i in range(self.size):
                for j in range(self.position[0]):
                    sys.stdout.write(" ")
                for j in range(self.size):
                    sys.stdout.write("#")
                sys.stdout.write("\n")
