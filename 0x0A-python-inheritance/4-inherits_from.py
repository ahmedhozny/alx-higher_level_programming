#!/usr/bin/python3

"""A module."""


def inherits_from(obj, a_class):
    """
    True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False
    """
    return issubclass(type(obj), a_class) or type(obj) is a_class
