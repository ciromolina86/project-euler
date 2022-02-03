"""
Counting Sundays

Problem 19
You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import datetime
import math
import time

monthDays = {'January': 31, 'February': 28, 'March': 31, 'April': 30,
             'May': 31, 'June': 30, 'July': 31, 'August': 31,
             'September': 30, 'October': 31, 'November': 30, 'December': 31}
# daysOfWeek = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
# daysOfWeek = {0: 'Saturday', 1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}
daysOfWeekISO = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}


def isCentury(year):
    return year % 1000 == 0


def isLeapYear(year):
    if year % 4 == 0:
        if isCentury(year):
            return year % 400 == 0
        else:
            return True
    else:
        return False


def leapYearsGenerator(start=1900):
    year = start
    while True:
        if isLeapYear(year):
            yield year
        year += 1


def sakamotoAlgorithm(year, month, day):
    """
    Compute day of week by using Sakamoto's algorithm

    :param year: year of desired day of week
    :param month: month of desired day of week
    :param day: day of desired day of week
    :return: day of week: 0 = Sunday, 1 = Monday, etc.
    """
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    if month < 3:
        year -= 1

    return int((year + year / 4 - year / 100 + year / 400 + t[month - 1] + day) % 7)


def gaussAlgorithm(year, month, day):
    """
    Compute day of week by using Gauss's algorithm

    https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week

    :param year: year of desired day of week
    :param month: month of desired day of week
    :param day: day of desired day of week
    :return: day of week: 0=Sunday … 6=Saturday
    """
    monthShift = [11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # months are numbered from 3 for March to 14 for February

    if month < 3:  # is the year minus 1 for January or February, and the year for any other month
        year -= 1

    # is the first 2 digits of Y
    c = year // 100

    # is the last 2 digits of Y
    y = year % 100

    # is the day of the month (1 to 31)
    d = day

    # is the shifted month (March=1,...January = 11, February=12)
    m = monthShift[month - 1]

    w = (d + math.floor(2.6 * m - 0.2) + y + math.floor(y / 4) + math.floor(c / 4) - 2 * c) % 7

    return w


def zellerAlgorithm(year=1900, month=1, day=1):
    """
    Compute day of week by using Zeller's algorithm

    https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week

    :param year: year of desired day of week
    :param month: month of desired day of week
    :param day: day of desired day of week
    :return: ISO day-of-week: 1 = Monday to 7 = Sunday
    """
    monthShift = [13, 14, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # months are numbered from 3 for March to 14 for February

    if month < 3:  # is the year minus 1 for January or February, and the year for any other month
        year -= 1

    # is the first 2 digits of Y
    c = year // 100

    # is the last 2 digits of Y
    y = year % 100

    # is the day of the month (1 to 31)
    d = day

    # is the shifted month (March=3,...January = 13, February=14)
    m = monthShift[month - 1]

    # is the day of week (1=Sunday,..0=Saturday)
    w = (d + math.floor(13 * (m + 1) / 5) + y + math.floor(y / 4) + math.floor(c / 4) - 2 * c) % 7

    # convert ISO 8601 standard day of week (1=Monday,..7=Sunday)
    w = ((w + 5) % 7) + 1

    return w


def getDayOfWeek(year=datetime.date.today().year, month=datetime.date.today().month, day=datetime.date.today().day):
    """
    Get the day of the week for a given date

    :return:
    """
    # dayOfWeek = sakamotoAlgorithm(year, month, day)
    # dayOfWeek = gaussAlgorithm(year, month, day)
    dayOfWeek = zellerAlgorithm(year, month, day)

    print(f'{year}-{month}-{day}: {daysOfWeekISO[dayOfWeek]}')


if __name__ == '__main__':
    start = time.time()

    # leapYears = leapYearsGenerator(1986)
    # for i in range(10):
    #     print(next(leapYears))

    print(getDayOfWeek(1777, 4, 30))
    print(getDayOfWeek(1855, 2, 23))
    print(getDayOfWeek(1900, 1, 1))
    print(getDayOfWeek(2022, 2, 2))
    print(getDayOfWeek(2022, 2, 3))
    print(getDayOfWeek(2022, 2, 4))
    print(getDayOfWeek(2022, 2, 5))
    print(getDayOfWeek(2022, 2, 6))

    end = time.time()
    print(f"{(end - start):.6f} seconds")
