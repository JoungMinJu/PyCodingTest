import sys
from collections import Counter

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
nums_count = Counter(nums)
result = [-1] * N
stack = [0]
'''
오등큰수를 찾지 못한 수의 index를 스택에 저장한다.
그리고 stack top의 index에 해당하는 수보다 등장 횟수가 더 많으면 
그 index에 해당하는 수의 오등큰수를 바꿔주기
'''

for i in range(1, N) :
    while stack and nums_count[nums[stack[-1]]] < nums_count[nums[i]] :
        result[stack.pop()] = nums[i]
    stack.append(i)
print(*result)