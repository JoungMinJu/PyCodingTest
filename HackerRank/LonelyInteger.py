import math
import os
import random
import re
import sys

from collections import defaultdict


def lonelyinteger(a):
    number_count = defaultdict(int)
    for i in a:
        number_count[i] += 1

    for key in number_count.keys():
        if number_count[key] == 1:
            return key


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
