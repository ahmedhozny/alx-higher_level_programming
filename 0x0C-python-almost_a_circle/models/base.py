#!/usr/bin/python3

"""Defines the base module."""

import json


class Base:
    """
    Base model. Parent of all shapes

    Attributes:
        __nb_objects (int): number of Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialise a new Base.

        Args:
            id (int): id of the new base.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def type_int_checker(name, value):
        """
        checks a given value is actually an int

        Args:
            name (any): name of the value.
            value (int): value to be checked
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    @staticmethod
    def from_json_string(json_string):
        """
        decodes JSON string to a python object

        Args:
            json_string (str): string to be decoded
        """
        if json_string is None or len(json_string) < 1:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        encodes a list dictionaries to a string using JSON

        Args:
            list_dictionaries (list): list to be encoded.
        """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves lists to objects to the perspective class file

        Args:
            list_objs (list): list of objects.
        """
        with open(cls.__name__ + ".json", "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                file.write(Base.to_json_string(
                    [o.to_dictionary() for o in list_objs])
                )

    @classmethod
    def load_from_file(cls):
        """
        loads perspective class file and creates objects
        """
        try:
            with open(cls.__name__ + ".json", "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        according to class the function was called from,
        creates object from given directory

        Args:
            **dictionary (dict): Key/value pairs of attributes.
        """
        if dictionary is not None and len(dictionary) > 0:
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1, 1)
            elif cls.__name__ == "Square":
                obj = cls(1, 1)
            else:
                return None
            obj.update(**dictionary)
            return obj
