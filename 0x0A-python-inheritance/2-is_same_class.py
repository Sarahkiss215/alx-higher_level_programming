#!/usr/bin/python3
"""Returns True if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Check if an object is an instance of the specified class"""

    return (type(obj) == a_class)
