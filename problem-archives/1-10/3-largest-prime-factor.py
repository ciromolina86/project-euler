"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


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


def getFactors(arg):
    """find all the factors of a given number"""
    return [num for num in range(1, arg + 1) if arg % num == 0]


def getPrimeNumbers(limit):
    """generate all primes smaller than or equal to n using Sieve of Eratosthenes"""
    primeMask = [True for i in range(limit + 1)]
    prime = 2

    while prime * prime <= limit:
        if primeMask[prime]:
            # Update all multiples of prime
            for i in range(prime * prime, limit + 1, prime):
                primeMask[i] = False
        prime += 1

    return [x for x in range(2, limit + 1) if primeMask[x]]


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


if __name__ == '__main__':
    import time

    start = time.time()

    print(getPrimeFactors(600851475143))

    end = time.time()
    print(f"{end - start} seconds")
