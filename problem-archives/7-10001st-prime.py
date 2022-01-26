"""
10001st prime

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math


def isPrime(arg):
    """check if number is prime"""
    # zero and one are not prime numbers
    if abs(arg) == 0 or abs(arg) == 1:
        return False

    # special case: two
    elif abs(arg) == 2:
        return True

    else:
        for i in range(2, int(arg ** 0.5) + 1):
            if arg % i == 0:
                return False
        return True


def primeNumberGenerator():
    """generate an infinite sequence of prime numbers"""
    limit = inc = 1_000_000
    idx = 0

    while True:
        primes = sieveOfEratosthenes(limit)

        for prime in primes[idx:limit]:
            yield prime

        limit += inc
        idx = len(primes)


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


def sieveOfAtkin(limit=10):
    """
    The sieve of Atkin: find all the prime numbers less than or equal to n

    :param limit: an integer n > 1
    :return: all prime numbers from 2 through n.
    """
    sieve = [False] * limit

    x = 1
    while x * x < limit:
        y = 1
        while y * y < limit:
            n = (4 * x * x) + (y * y)
            if n <= limit and (n % 60 == 1 or n % 60 == 5):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 60 == 7:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if x > y and n <= limit and n % 60 == 11:
                sieve[n] ^= True
            y += 1
        x += 1

    r = 5
    while r * r < limit:
        if sieve[r]:
            for i in range(r * r, limit, r * r):
                sieve[i] = False
        r += 1

    return [2, 3, 5] + [i for i in range(5, limit) if sieve[i]]


if __name__ == '__main__':
    import time

    start = time.time()

    # print(sieveOfEratosthenes(1000000))  # 0.151100 seconds
    # print(sieveOfAtkin(1000000))  # 0.436244 seconds

    primes = primeNumberGenerator()
    nth = 10_001
    for i in range(1, nth + 1):
        prime = next(primes)
        # print(f'{i}th - {prime}')
        if i == nth:
            print(f'{i}th prime = {prime}')

    end = time.time()
    print(f"{(end - start):.6f} seconds")
