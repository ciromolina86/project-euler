"""
Largest palindrome product

Problem 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def isPalindrome(arg):
    """check if a number is palindrome"""
    return str(arg) == str(arg)[::-1]


def getTwoDigitPalindromicMultiples():
    palindromicNumbers = []

    for i in range(99, 10, -1):
        for j in range(99, 10, -1):
            if isPalindrome(i * j):
                palindromicNumbers.append(i * j)

    return palindromicNumbers


def getThreeDigitPalindromicMultiples():
    palindromicNumbers = []

    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if isPalindrome(i * j):
                palindromicNumbers.append(i * j)

    return palindromicNumbers


if __name__ == '__main__':
    import time

    start = time.time()

    # print(max(getTwoDigitPalindromicMultiples()))
    print(max(getThreeDigitPalindromicMultiples()))

    end = time.time()
    print(f"{end - start} seconds")
