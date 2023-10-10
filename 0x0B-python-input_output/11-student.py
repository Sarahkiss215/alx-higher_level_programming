#!/usr/bin/python3
"""Module 11-student.py"""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        retatt = {}
        if attrs is not None:
            keys = [k for k in self.__dict__ if k in attrs]
        else:
            keys = [k for k in self.__dict__]

        for k in keys:
            val = getattr(self, k)
            if type(val) in [list, dict, str, int, bool]:
                retatt[k] = val
        return (retatt)
