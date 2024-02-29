#!/usr/bin/python3
"""
Change comes from within
"""


def help(start, end, coins, total, number, time):
    """
    backtracking recursion
    that helps to find the number
    """
    if start > end:
        return -1
    while coins[start] + number <= total:
        number += coins[start]
        time += 1
    if number == total:
        return time
    return help(start + 1, end, coins, total, number, time)


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.
    """
    if total <= 0:
        return 0
    sorted_coins = sorted(coins, reverse=True)
    return help(0, len(sorted_coins) - 1, sorted_coins, total, 0, 0)
