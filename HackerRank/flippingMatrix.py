
import math
import os
import random
import re
import sys


def flippingMatrix(matrix):
    n = len(matrix)
    s = 0
    for i in range(n//2) :
        for j in range(n//2) :
            s += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
