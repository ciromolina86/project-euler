"""
Sum square difference

Problem 6
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def square(arg):
    return arg ** 2


def getSumOfSquares(start=1, stop=10):
    return sum(map(square, [x for x in range(start, stop + 1)]))


def getSquareOfSum(start=1, stop=10):
    return square(sum([x for x in range(start, stop + 1)]))


if __name__ == '__main__':
    import time

    start = time.time()

    print(f'the difference between the sum of the squares of the first one hundred natural numbers and '
          f'the square of the sum is: {getSquareOfSum(start=1, stop=100) - getSumOfSquares(start=1, stop=100)}')

    end = time.time()
    print(f"{end - start} seconds")
