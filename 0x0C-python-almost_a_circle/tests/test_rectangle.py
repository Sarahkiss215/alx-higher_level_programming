#!/usr/bin/python3
"""Test for rectangle.py module"""

import unittest
import json
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Defines TestBaseClass"""

    @classmethod
    def setClass(cls):
        cls.one = Base()
