#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return
    for list in matrix:
        for digit in list:
            if digit != list[-1]:
                print("{:d} ".format(digit), end='')
            else:
                print("{:d}".format(digit), end = ' ')
        print()
