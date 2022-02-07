"""
Longest Collatz sequence

Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import math
import time


def isMultipleOf2(arg):
    """check if argument is multiple de 23"""
    if arg % 2 == 0:
        return True
    else:
        return False


def isEven(arg):
    """check if argument is even"""
    return isMultipleOf2(arg)


def collatzSequenceGenerator(n=100):
    """ Generate a Collatz Sequence """
    yield n

    while n > 1:
        if isEven(n):
            n //= 2
        else:
            n = 3 * n + 1
        yield n


if __name__ == '__main__':
    start = time.time()

    count = 0
    number = 0
    for n in range(int(math.sqrt(1_000_000)),1_000_000):
        collatz = collatzSequenceGenerator(n)

        _count = 0
        for x in collatz:
            _count += 1

            if _count > count:
                count = _count
                number = n

    print(f'number:{number}, count:{count}')

    end = time.time()
    print(f"{(end - start):.6f} seconds")
