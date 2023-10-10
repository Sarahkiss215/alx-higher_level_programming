#!/usr/bin/python3
"""Defines class Myclass"""


class MyList(list):
    """Defines class MyList that inherits from list"""

    def print_sorted(self):
        print(sorted(self))
