#!/usr/bin/python3
"""Prime Game"""

# def isPrime(n):
#     """check if the number is prime"""
#     if n == 1:
#         return False
#     for i in range(2, int(n/2) + 1):
#         if n % i == 0:
#             return False
#     return True


# def count_prime(req_list):
#     """check if one item in list is prime"""
#     count = 0
#     for one in req_list:
#         if isPrime(one):
#             count += 1
#     return count


def count_primes(n):
    """check if one item in list is prime"""
    number = 0
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            number += 1
            for i in range(p, n + 1, p):
                sieve[i] = False
    return number


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
        count_p = count_primes(num)
        if count_p % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1
    if players['Ben'] > players['Maria']:
        return 'Ben'
    if players['Maria'] > players['Ben']:
        return 'Maria'
    return None


# def isWinner(x, nums):
#     """ Determine the winner of the game. """
#     if not x or not nums:
#         return None
#     maria_count = ben_count = 0
#     for num in nums[:x]:
#         primes = get_primes(num)
#         if len(primes) % 2 == 0:
#             ben_count += 1
#         else:
#             maria_count += 1
#     if maria_count > ben_count:
#         return 'Maria'
#     elif ben_count > maria_count:
#         return 'Ben'
#     return None
