import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
works = []
visited = [0] * 1001
for _ in range(N) :
    d, w = map(int, input().split())
    works.append((d, w))

works.sort(key = lambda x : (-x[1]))
answer = 0
for day, worth in works :
    i  = day
    while i > 0 and visited[i] :
        i-= 1 # 과제를 할 날짜 탐색
    if i == 0 :
        continue #과제할 날짜 없음 패스
    visited[i] = 1
    answer += worth
print(worth)
# 무조건 좋은 점수를 얻는 것이 중요하기 때문에 그리디
# 점수로 내림차순 정렬하되, 그 과제 먹으려면 최대한 나중에 수행하는 쪽
