#!/usr/bin/python3
"""Module 12-pascal_triangle.py"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return ([])

    tri = [[1]]
    while len(tri) != n:
        t = tri[-1]
        tmp = [1]
        for i in range(len(t) - 1):
            tmp.append(t[i] + t[i + 1])
        tmp.append(1)
        tri.append(tmp)
    return (tri)
