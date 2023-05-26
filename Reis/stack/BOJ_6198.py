from collections import deque
import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
heights = [int(input()) for _ in range(N)]

stack = deque()
answer = 0
for height in heights :
    if not stack or stack[0] > height :
        stack.appendleft(height)
    else :
        while stack and stack[0] <= height :
            stack.popleft()
        stack.appendleft(height)
    answer += len(stack)-1
print(answer)