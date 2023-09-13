#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """ Returns a new dictionary with all values multiplied by 2 """
    return ({i: a_dictionary[i] * 2 for i in a_dictionary})
