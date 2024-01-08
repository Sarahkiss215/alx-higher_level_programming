#!/usr/bin/python3
""" Contain the complexity of your algorithm:
O(log(n)), O(n), O(nlog(n)) or O(n2)
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if type(list_of_integers) != list:
        return
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]

