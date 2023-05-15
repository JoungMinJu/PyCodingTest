import math
import os
import random
import re
import sys

def plusMinus(arr):
    plus = minus = zero = 0
    for i in arr:
        if i == 0:
            zero += 1
        elif i < 0:
            minus += 1
        else:
            plus += 1
    print(plus / len(arr))
    print(minus / len(arr))
    print(zero / len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
