#!/usr/bin/python3

"""Defines the square module."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, let's create squares.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialise a new Square.

        Args:
            id (int): id of the new Square.
        """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """
        Updates instance attributes

        Args:
            *args (ints): New attribute values.
                - 1st argument should be the id attribute
                - 2nd argument should be the size attribute
                - 3rd argument should be the x attribute
                - 4th argument should be the y attribute

            **kwargs (dict): New key/value pairs of attributes.
        """
        for i in range(len(args)):
            if i == 0:
                if args[i] is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = args[0]
            elif i == 1:
                self.width = args[1]
                self.height = args[1]
            elif i == 2:
                self.x = args[2]
            elif i == 3:
                self.y = args[3]

        if len(args) < 1:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.width = value
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
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Returns string representing the instance
        """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
