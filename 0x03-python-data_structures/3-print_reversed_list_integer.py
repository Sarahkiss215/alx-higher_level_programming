#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if not my_list:
        pass
    else:
        my_list.reverse()
        for digits in range(len(my_list)):
            print("{:d}".format(my_list[digits]))