"""
Summation of primes

Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time
import numpy as np


def sieveOfEratosthenes(n=11):
    """
    The sieve of Eratosthenes: find all the prime numbers less than or equal to n

    :param n: an integer n > 1
    :return: all prime numbers from 2 through n.
    """
    sieve = [True for x in range(n + 1)]  # prime number mask
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    i = 2
    while i ** 2 <= n:
        if sieve[i]:
            for j in range(i ** 2, n + 1, i):
                sieve[j] = False
        i += 1

    return [i for i in range(n + 1) if sieve[i]]


def summationOfPrimesLessThan(limit=2_000_000):
    return sum(sieveOfEratosthenes(limit))


if __name__ == '__main__':
    print(summationOfPrimesLessThan())
