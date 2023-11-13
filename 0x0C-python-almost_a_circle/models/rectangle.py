#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialise a new Rectangle.

        Args:
            id (int): id of the new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """
        returns area of the Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays a Rectangle as a representation of "#"
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            [print(" ", end="") for _ in range(self.x)]
            [print("#", end="") for _ in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """
        Updates instance attributes

        Args:
            *args (ints): New attribute values.
                - 1st argument should be the id attribute
                - 2nd argument should be the width attribute
                - 3rd argument should be the height attribute
                - 4th argument should be the x attribute
                - 5th argument should be the y attribute

            **kwargs (dict): New key/value pairs of attributes.
        """
        for i in range(len(args)):
            if i == 0:
                if args[i] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = args[0]
            elif i == 1:
                self.width = args[1]
            elif i == 2:
                self.height = args[2]
            elif i == 3:
                self.x = args[3]
            elif i == 4:
                self.y = args[4]

        if len(args) < 1:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns a dictionary of Rectangle attributes.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Returns string representing the instance
        """

        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
                .format(self.id, self.x, self.y, self.width, self.height))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        Base.type_int_checker("width", width)
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        Base.type_int_checker("height", height)
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        Base.type_int_checker("x", x)
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        Base.type_int_checker("y", y)
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
