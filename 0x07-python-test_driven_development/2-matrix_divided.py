#!/usr/bin/python3

"""A module for dividing matrices."""


def matrix_divided(matrix, div):
    """
    Divides a matrix by given value.

    Args:
        matrix (list): The first integer or float.
        div (int or float): The second integer or float, defaults to 98.
    """
    if (not isinstance(matrix, list) or
            False in [isinstance(_, list) for _ in matrix]):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(_) for _ in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        ZeroDivisionError("division by zero")
    return list(map(lambda x: list(
        map(lambda y: round(y / div, 2), x)
    ), matrix))
