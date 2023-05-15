import math
import os
import random
import re
import sys


def timeConversion(s):
    hours, minutes, seconds_AMPM = s.split(":")
    if seconds_AMPM[2:] == "PM" and hours != '12':
        hours = str(int(hours) + 12)
    if seconds_AMPM[2:] == "AM" and hours == '12':
        hours = "00"
    if seconds_AMPM[2:] == "PM" and hours == '12':
        hours = "12"

    conversion_time = hours + ':' + minutes + ':' + seconds_AMPM[0:2]

    return conversion_time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
