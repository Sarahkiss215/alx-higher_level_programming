#!/usr/bin/python3
""" Prints a square with the character # """


def print_square(size):
    """ Prints a square """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((('#' * size) + '\n') * size, end=("" if size else "\n"))
