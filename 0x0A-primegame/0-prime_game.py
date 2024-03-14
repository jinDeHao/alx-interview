#!/usr/bin/python3
"""Prime Game"""


def isPrime(n):
    """check if the number is prime"""
    if n == 1:
        return False
    for i in range(2, int(n/2)):
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
    palyer = {"Maria": 0, "Ben": 0}
    primeList = [i for i in range(2, 10001) if isPrime(i)]
    for n in nums:
        round = [i for i in range(1, n+1)]
        i = 0
        for r in primeList:
            name = 'Maria'
            if i % 2 == 0:
                name = 'Ben'
            if not still_prime(round):
                palyer[name] += 1
                break
            m = []
            for num in round:
                if num % r == 0:
                    m.append(num)
            all(round.remove(j) for j in m)
            i += 1
    if palyer['Ben'] > palyer['Maria']:
        return 'Ben'
    if palyer['Maria'] > palyer['Ben']:
        return 'Maria'
    return None


# print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
