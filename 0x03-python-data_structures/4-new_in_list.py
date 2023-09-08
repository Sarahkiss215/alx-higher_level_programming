#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    list_len = len(my_list)
    if idx > list_len:
        return (my_list)
    new_list = my_list[:]
    new_list[idx] = element
    return (new_list)
