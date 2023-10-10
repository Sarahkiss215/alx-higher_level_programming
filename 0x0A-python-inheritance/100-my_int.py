#!/usr/bin/python3
"""Defines a class MyInt"""


class MyInt(int):
    """Class MyInt that inherits from int"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
