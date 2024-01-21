#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n: int) -> int:
    """
    method that calculates
    the fewest number of
    operations needed to
    result in exactly n
    H characters in the file.
    """
    if n <= 1:
        return 0
    cnoc = 1
    opNum = 1
    clipboard_size = 1
    while cnoc <= n:
        if cnoc != 1 and n % cnoc == 0:
            clipboard_size = cnoc / clipboard_size
        cnoc += clipboard_size
        opNum += 1
    return (opNum)
