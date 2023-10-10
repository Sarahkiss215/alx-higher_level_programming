#!/usr/bin/python3
"""Inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file"""
    txt = ""
    with open(filename) as p:
        for line in p:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
