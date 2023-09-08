#!/usr/bin/python3
def max_integer(my_list=[]):
    list_len = len(my_list)
    if list_len == 0:
        return (None)
    max_digit = my_list[0]
    for digit in range(1, list_len):
        if my_list[digit] > max_digit:
            max_digit = my_list[digit]
    return (max_digit)
