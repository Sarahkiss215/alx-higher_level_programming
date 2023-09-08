#!/usr/bin/python3
def no_c(my_string):
    str_len = len(my_string)
    new_string = my_string[:]

    i = 0
    for letter in range(str_len):
         if (my_string[letter] == 'c' or my_string[letter] == 'C'):
            new_string = new_string[:(letter - i)] + my_string[(letter + 1):]
            i += 1
    return (new_string)

