#!/usr/bin/python3
def best_score(a_dictionary):
    """ Returns a key with the biggest integer value """
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret_k = list(a_dictionary.keys())[0]
    big_val = a_dictionary[ret_k]
    for n, m in a_dictionary.items():
        if m > big_val:
            big_val = m
            ret_k = n
    return (ret_k)
