#!/usr/bin/python3
"""Module 1-write_file.py"""


def write_file(filename="", text=""):
    """
    rites a string to a text file (UTF8) and returns
    the number of characters written
    """
    wfile = 0
    with open(filename, "w", encoding="utf-8") as f:
        wfile = f.write(text)

    return (wfile)
