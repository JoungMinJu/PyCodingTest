import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()
N, K = map(int, input().split())

# lst = 문자 길이 저장
# nums = 각 길이의 문자가 몇 개 있는지 저장하는 dict
# 문자열 들어올 때마다 K범위 안에서 세어 더해주기

lst = []
nums = dict()
cnt = 0
for i in range(N) :
    lst.append(len(input()))
    if not lst[i] in nums : # 등장한 적 없는 글자수
        nums[lst[i]] = 0  # 초기화 해주기
    if i > K :
        nums[list[i-K-1]] -= 1 # 넘어가면 -1
    cnt += nums[lst[i]]
    nums[lst[i]] += 1
print(cnt)