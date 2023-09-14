#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ Deletes keys with a specific value in a dictionary """
    while value in a_dictionary.values():
        for index_key, val in a_dictionary.items():
            if val == value:
                del a_dictionary[index_key]
                break

    return (a_dictionary)
