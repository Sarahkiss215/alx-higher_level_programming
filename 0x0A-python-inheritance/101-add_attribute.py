#!/usr/bin/python3
"""Adds a new attribute to an object if it’s possible"""


def add_attribute(self, attribute, value):
    """Adds a new attribute to an object if it’s possible"""
    if hasattr(self, '__dict__'):
        setattr(self, attribute, value)
    else:
        raise TypeError("can't add new attribute")
