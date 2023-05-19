# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

q = int(input())
input_stack = deque()
output_stack = deque()
for _ in range(q):
    commands = list(map(int, input().split()))
    if commands[0] == 1:
        input_stack.append(commands[1])
    elif commands[0] == 2:
        if not output_stack:
            while input_stack:
                output_stack.append(input_stack.pop())
        if output_stack:
            output_stack.pop()
    elif commands[0] == 3:
        if not output_stack:
            while input_stack:
                output_stack.append(input_stack.pop())
        if output_stack:
            print(output_stack[-1])

