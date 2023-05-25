import sys
from heapq import heappop, heappush
input = lambda : sys.stdin.readline().rstrip()

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y) :
    x = find(x)
    y = find(y)
    if x > y :
        parent[y] = x
    elif x < y :
        parent[x] = y

N = int(input())
stars = [list(map(float, input().split())) for _ in range(N)]
dist = []
parent = [i for i in range(N)]
for one in range(N) :
    for two in range(N) :
        if one == two :
            continue
        one_x, one_y = stars[one]
        two_x, two_y = stars[two]
        now_dist = ((two_x - one_x) **2 + (two_y - one_y)**2)**0.5
        heappush(dist, [round(now_dist,2), one, two])

answer = 0
while dist :
    weight, one, two = heappop(dist)
    if find(one) != find(two) :
        answer += weight
        union(one, two)
print(answer)
