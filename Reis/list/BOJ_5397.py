import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for test in range(T) :
    log = list(input())
    rstack = deque()
    lstack = deque()
    for i in log :
        if i == '-' :
            if lstack : # 값이 있으면
                lstack.pop()
        elif i == '<' :
            if lstack :
                rstack.append(lstack.pop())
        elif i == ">" :
            if rstack :
                lstack.append(rstack.pop())
        else :
            lstack.append(i)

    print(''.join(lstack) + "".join(reversed(rstack)))