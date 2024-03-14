#!/usr/bin/python3
"""Prime Game"""


def count_primes(n):
    """check if one item in list is prime"""
    number = 0
    # sieve = [True] * (n + 1)
    # for p in range(2, n + 1):
    #     if sieve[p]:
    #         number += 1
    #         for i in range(p, n + 1, p):
    #             sieve[i] = False
    round = [i for i in range(1, n+1)]
    for r in round:
        is_not = False
        if r == 1:
            continue
        for i in range(2, int(r**0.5) + 1):
            if r % i == 0:
                is_not = True
                break
        if not is_not:
            number += 1
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

def test_isWinner():
    test_cases = [
        ((3, [3, 4, 5]), "Ben"),
        ((2, [5, 6]), "Maria"),
        ((4, [7, 8, 9, 10]), "Ben"),
        ((3, [11, 12, 13]), "Maria"),
        ((2, [14, 15]), "Ben"),
    ]

    for inputs, expected in test_cases:
        x, nums = inputs
        result = isWinner(x, nums)
        if result != expected:
            print(f"Test case failed: For inputs {inputs}, expected {expected}, but got {result}")
            return

    print("All test cases passed!")

# Call the tester function
test_isWinner()
