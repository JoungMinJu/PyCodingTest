import math
import os
import random
import re
import sys


def countingSort(arr):
    number_count = [0] * 100
    for num in arr :
        number_count[num] += 1
    return number_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
