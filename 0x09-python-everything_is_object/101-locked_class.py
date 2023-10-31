#!/usr/bin/python3

"""Module that is about locked class."""


class LockedClass:
    """
    Only permit attribute creation for those named first_name.
    """
    __slots__ = ["first_name"]
