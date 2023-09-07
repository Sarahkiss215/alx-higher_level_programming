#!/usr/bin/python3
def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for digit in range(4, 6):
            c = add(c, digit)
        return (c)
    else:
        return(sub(a, b))
