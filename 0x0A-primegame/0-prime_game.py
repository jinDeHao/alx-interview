#!/usr/bin/python3
"""Prime Game"""


def isPrime(n):
    """check if the number is prime"""
    if n == 1:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True


def count_prime(req_list):
    """check if one item in list is prime"""
    count = 0
    for one in req_list:
        if isPrime(one):
            count += 1
    return count


def isWinner(x, nums):
    """
    Maria and Ben are playing a game.
    Given a set of consecutive integers starting
    from 1 up to and including n, they take turns
    choosing a prime number from the set and removing that
    number and its multiples from the set.
    The player that cannot make a move loses the game.
    """
    if x == 0 or len(nums) == 0:
        return None
    players = {"Maria": 0, "Ben": 0}
    for num in nums[:x]:
        count_p = count_prime([i for i in range(1, num + 1)])
        if count_p % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1
    if players['Ben'] > players['Maria']:
        return 'Ben'
    if players['Maria'] > players['Ben']:
        return 'Maria'
    return None
