#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    if len(s) % 2 == 1:
        return "NO"
    stack = deque()
    for i in range(len(s)):
        now_char = s[i]
        if now_char in ["{", "(", "["]:
            stack.append(now_char)
        else:
            if not stack:
                return "NO"
            before_char = stack.pop()
            if not check_is_mate(before_char, now_char):
                return "NO"
    if stack:
        return "NO"
    return "YES"


def check_is_mate(before, now):
    if now == ")":
        return before == "("
    if now == "]":
        return before == "["
    if now == "}":
        return before == "{"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
