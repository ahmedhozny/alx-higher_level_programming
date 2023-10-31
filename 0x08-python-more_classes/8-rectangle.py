#!/usr/bin/python3

"""Defines a class Rectangle."""


class Rectangle:
    """Represents a Rectangle.

    Attributes:
        number_of_instances (int):  number of Rectangle instances.
        print_symbol (str): symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = '#'

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string with '#' character for rectangle width and height."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = ""
        for _ in range(self.__height):
            rect += str(Rectangle.print_symbol) * self.__width + "\n"
        return rect.rstrip()

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = ("Rectangle(" + str(self.__width) + ", "
                + str(self.__height) + ")")
        return rect

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
