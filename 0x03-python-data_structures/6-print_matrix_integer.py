#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for digits in range(len(matrix)):
        for a in range(len(matrix[digits])):
            if a != 0:
                print(" ", end='')
            print("{:d}".format(matrix[digits][a]), end='')
        print()
