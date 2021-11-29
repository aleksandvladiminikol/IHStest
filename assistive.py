import datetime
import settings
import random


def readResult(result):
    for i in result:
        print(i)


def getrndmdate():
    ActYear = datetime.datetime.today().year
    StartYear = settings.startdate.year

    year = random.randint(StartYear, ActYear)
    month = random.randint(1, 12)
    leapmonth = (1, 3, 5, 7, 8, 10, 12)
    febr = 2

    if month == febr:
        limitday = 28
    elif month in leapmonth:
        limitday = 31
    else:
        limitday = 30

    day = random.randint(1, limitday)

    return datetime.datetime(year, month, day, 0, 0, 0)
