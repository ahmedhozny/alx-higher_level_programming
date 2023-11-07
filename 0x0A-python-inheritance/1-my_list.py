#!/usr/bin/python3

"""A module."""


class MyList(list):
    """MyList that inherits from list."""

    def print_sorted(self):
        """That prints the list, but sorted (ascending sort)."""
        print(sorted(self))
