"""
Highly divisible triangular number

Problem 12
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
import time
import math
import numpy as np
from collections import Counter


def getPrimeFactors(arg, primes=None):
    """find all the prime factors of a number using prime factorization by division"""

    if primes is None:
        primes = []

    for num in range(2, int(arg ** 0.5) + 1):
        if arg % num == 0:
            primes.append(num)
            break
    else:
        primes.append(arg)
        return primes

    return getPrimeFactors(arg // num, primes)


def getNumberOfFactors(num):
    """
    get the number of factors by using prime factorization

    # of factors = (a+1) * (b+1) * (c+1), where: num = x^a * y^b * z^c
    https://www.cuemath.com/numbers/factors/
    """
    primes = getPrimeFactors(num)
    powers = Counter()

    for prime in primes:
        powers[prime] += 1

    powers = list(map(lambda x: x + 1, powers.values()))

    return np.prod(powers)


def triangleNumberGenerator():
    """
    triangular numbers generator

    Tn = n(n+1)/2
    https://en.wikipedia.org/wiki/Triangular_number
    """
    nth = 1

    while True:
        yield int(nth * (nth + 1) / 2)
        nth += 1


if __name__ == '__main__':
    start = time.time()

    triangularNumbers = triangleNumberGenerator()

    while True:
        num = next(triangularNumbers)

        if getNumberOfFactors(num) > 500:
            print(f'{num}')
            break

    end = time.time()
    print(f"{(end - start):.6f} seconds")
