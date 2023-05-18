from collections import deque
import sys
input = sys.stdin.readline

left = deque(input().rstrip())
right = deque()
N = int(input().rstrip())
length = len(left)


for i in range(N):
    order = list(map(str, input().split()))
    if order[0] == "P":
        left.append(order[1])
    if order[0] == "L":
        if len(left) != 0:
            right.appendleft(left.pop())
    if order[0] == "D":
        if len(right) != 0:
            left.append(right.popleft())
    if order[0] == "B":
        if len(left) != 0:
            left.pop()

print("".join(left + right))