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
    check if the island id valid
    """
    if not isinstance(grid, list) or grid == [] or\
            not all(isinstance(g, list) for g in grid) or grid == [[]]:
        return 0
    Len.h = len(grid)
    Len.w = len(grid[0])
    if grid == [[0]*Len.w]*Len.h:
        return 0
    return 1


def count_perimerter(grid, x, y):
    """
    perimerter counter
    """
    p = 0
    if x-1 < 0 or grid[x-1][y] == 0:
        p += 1
    if y+1 >= Len.w or grid[x][y+1] == 0:
        p += 1
    if x+1 >= Len.h or grid[x+1][y] == 0:
        p += 1
    if y-1 < 0 or grid[x][y-1] == 0:
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
