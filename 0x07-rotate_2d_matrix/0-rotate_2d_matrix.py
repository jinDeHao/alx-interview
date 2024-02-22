#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix,
    rotate it 90 degrees clockwise
    """
    x = len(matrix)
    y = len(matrix[0])
    new_matrix = [[] for i in range(x)]
    for i in range(x):
        for j in range(y):
            new_matrix[j].append(matrix[i][j])
    for i in range(x):
        new_matrix[i].reverse()
        matrix[i] = new_matrix[i]
