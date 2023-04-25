import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
heights = []
for _ in range(N):
    heights.append(int(input()))

stack = deque()
stack.appendleft(0)
answer = -1
for idx in range(1, N) :
    now = heights[idx]
    while stack and heights[stack[0]] > now :
        before_x = stack.popleft()
        if len(stack) >= 1 :
            left = stack[0] + 1
        else :
            left = 0
        right = idx -1
        length = right - left + 1
        answer = max(answer, heights[before_x] * length)
    stack.appendleft(idx)

while stack :
    before_x = stack.popleft()
    if len(stack) >= 1:
        left = stack[0] + 1
    else:
        left = 0
    right = N-1
    length = right - left + 1
    answer = max(answer, heights[before_x] * length)

print(answer)
'''
모든 막대 x에 대해서, x를 높이로 하면서 만들 수 있는 가장 큰 직사각형 찾기
x의 왼쪽의 막대 중에 X보다 높이가 작은 첫 번째 막대 left, x보다 높이가 작은 첫 번째 막대 right 찾아야함

스택에 막대를 하나씩 넣기 전에, 스택의 가장 위에 있는 막대 top과 현재 넣으려고하는 막대 비교
top보다 크면 top을 높이로하는 직사각형 x를 지날 수 없음
top을 높이로 하는 직시각혁의 right = x-1
top을 높이로하면 let는 top 다음에 스택에 들어있는 막대!!

이거 끝나고 스택이 비어있지 않으면 ?? right가 가장 오른쪽 끝인 경우
스택에 있는 막대를 하나씩 뺴면서 위의 과정을 반복
'''
