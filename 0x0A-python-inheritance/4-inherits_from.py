#!/usr/bin/python3
"""Module 4-inherits_from.py"""


def inherits_from(obj, a_class):
    """Checks if an object is directly or indirectly from an inherited class"""

    return ((issubclass(type(obj), a_class)) and type(obj) != a_class)
