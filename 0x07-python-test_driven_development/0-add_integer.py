#!/usr/bin/python3
"""
    This is the 0-add_integer module
    It supplies one function, add_integer.
    For example, >>> add_integer(5, 9)
"""


def add_integer(a, b=98):
    """
    Adds two integers
    Arguments:
        a: integer or float
        b: integer or float
    Return: sum of a and b
    """
    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")

    if type(b) is not int:
        raise TypeError("b must be an integer")

    return (a + b)
