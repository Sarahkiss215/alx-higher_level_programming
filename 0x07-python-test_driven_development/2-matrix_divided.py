#!/usr/bin/python3
""" Divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ Divides all elements o fa matrix """

    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    err_m = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(err_m)

    rsize = 0
    if matrix and type(matrix[0]) is list:
        rsize = len(matrix[0])

    new_matrix = []
    for row in matrix:
        nrow = []
        if type(row) is not list:
            raise TypeError(err_m)

        if len(row) != rsize:
            raise TypeError("Each row of the matrix must have the same size")

        for index in range(rsize):
            val = row[index]
            if type(val) is not int and type(val) is not float:
                raise TypeError(err_m)
            nrow.append(round(val / div, 2))

        new_matrix.append(nrow)

    return (new_matrix)
