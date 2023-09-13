#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
     replaces all occurrences of an element by another in a new list

     my_list is the initial list
    search is the element to replace in the list
    replace is the new element
    """
    new_list = my_list[:]
    for digit in range(len(new_list)):
        if new_list[digit] == search:
            new_list[digit] = replace
    return (new_list)
