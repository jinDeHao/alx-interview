#!/usr/bin/python3
"""
Island Perimeter
"""


class Len:
    """
    class of paramiter
    """
    h = 0
    w = 0


def valid_island(grid):
    """
    check of the island id valid
    """
    if grid == [] or grid == [[]] or not isinstance(grid[0], list):
        return 0
    Len.h = len(grid)
    Len.w = len(grid[0])
    if grid == [[0]*Len.w]*Len.h or\
            grid == [[1]*Len.w]*Len.h:
        return 0
    return 1


def count_perimerter(grid, x, y):
    """
    perimerter counter
    """
    p = 0
    if x-1 >= 0 and grid[x-1][y] == 0:
        p += 1
    if y+1 < Len.w and grid[x][y+1] == 0:
        p += 1
    if x+1 < Len.h and grid[x+1][y] == 0:
        p += 1
    if y-1 >= 0 and grid[x][y-1] == 0:
        p += 1
    return p


def walker(grid, x=0, y=0, perimeter=0):
    """
    walk around the island
    """
    if y == Len.w:
        if x == Len.h - 1:
            return perimeter
        x += 1
        y = 0
    if grid[x][y] == 1:
        perimeter += count_perimerter(grid, x, y)
    return walker(grid, x, y+1, perimeter)


def island_perimeter(grid):
    """
    Island Perimeter
    """
    if not valid_island(grid):
        return 0
    return walker(grid)


print(island_perimeter([
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]))
