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


def still_prime(req_list):
    """check if one item in list is prime"""
    for one in req_list:
        if isPrime(one):
            return True
    return False


def isWinner(x, nums):
    """
    Maria and Ben are playing a game.
    Given a set of consecutive integers starting
    from 1 up to and including n, they take turns
    choosing a prime number from the set and removing that
    number and its multiples from the set.
    The player that cannot make a move loses the game.
    """
    if not x or not nums:
        return None
    player = {"Maria": 0, "Ben": 0}
    primeList = [i for i in range(2, 10001) if isPrime(i)]
    for n in nums[:x]:
        round = [i for i in range(1, n+1)]
        i = 0
        for r in primeList:
            name = 'Ben'
            if i % 2 == 0:
                name = 'Maria'
            if not still_prime(round):
                player[name] -= 1
                break
            m = []
            for num in round:
                if num % r == 0:
                    m.append(num)
            for j in m:
                round.remove(j)
            i += 1
    if player['Ben'] > player['Maria']:
        return 'Ben'
    if player['Maria'] > player['Ben']:
        return 'Maria'
    return None

def test_isWinner():
    test_cases = [
        ((3, [3, 4, 5]), "Ben"),
        ((2, [5, 6]), "Maria"),
        ((4, [7, 8, 9, 10]), "Maria"),
        ((3, [11, 12, 13]), "Maria"),
        ((2, [14, 15]), None),
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
