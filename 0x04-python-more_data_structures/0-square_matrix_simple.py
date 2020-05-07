#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda n: n**2, sq_list)) for sq_list in matrix]
