#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print()
    else:
        for list in matrix:
            for digit in list:
                if digit != list[-1]:
                    print("{:d} ".format(digit), end='')
                else: 
                    print("{:d}".format(digit))
