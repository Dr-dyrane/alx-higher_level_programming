#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ai in range(len(matrix)):
        for jay in range(len(matrix[ai])):
            if jay == len(matrix[ai]) - 1:
                print("{:d}".format(matrix[ai][jay]), end="")
            else:
                print("{:d} ".format(matrix[ai][jay]), end="")
        print()
