"""
Multiples of 3 or 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def isMultipleOf3(arg):
    """check if argument is multiple de 3"""
    if arg % 3 == 0:
        return True
    else:
        return False


def isMultipleOf5(arg):
    """check if argument is multiple de 5"""
    if arg % 5 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    multiplesOf3Or5 = []
    sumOfAllMultiplesOf3Or5 = 0

    for num in range(1000):
        if isMultipleOf3(num) or isMultipleOf5(num):
            multiplesOf3Or5.append(num)

    sumOfAllMultiplesOf3Or5 = sum(multiplesOf3Or5)

    print(sumOfAllMultiplesOf3Or5)
