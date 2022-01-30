"""
Number letter counts

Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""
import math
import time
from num2words import num2words


class Number(object):
    """OOP approach"""

    def __init__(self, value):
        self.value = value
        self.word = self.toWord2()
        self.numberToWord = {1: 'one', 2: 'two'}

    def toWord1(self):
        return self.numberToWord.get(self.value)

    def toWord2(self):
        return num2words(self.value)


def getLettersCount(words: str):
    """
    Get the number of letter in the words string

    :param words: string to be counted
    :return: number of letters
    """
    count = 0

    for letter in words:
        if letter != ' ' and letter != '-':
            count += 1

    return count


def getNumberLettersCount(start=1, end=1000):
    """
    Get the number of letters that are used if all the numbers from start to end (inclusive)
    were written out in words, except spaces and hyphens.

    :param start: start number of range
    :param end: end number of range
    :return: number of letters
    """
    count = 0

    for num in range(start, end+1):
        count += getLettersCount(num2words(num))

    return count


if __name__ == '__main__':
    start = time.time()

    print(getNumberLettersCount())

    end = time.time()
    print(f"{(end - start):.6f} seconds")
