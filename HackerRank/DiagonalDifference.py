import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    first = second = 0
    for row in range(len(arr)) :
        first += arr[row][row]
        second += arr[row][len(arr)-1-row]
    return abs(first-second)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
