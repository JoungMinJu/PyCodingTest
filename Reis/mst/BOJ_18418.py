'''
총 두 번의 MST
1. 내리막길을 먼저 연결해주는 방법
2. 오르막길을 먼저 연결해주는 방법
'''

import sys

input = lambda : sys.stdin.readline().rstrip()

def find(x) :
    if x != parent[x] :
        parent[x] = find(parent[x])
    return parent[x]

N, M = map(int, input().split())
edge = []
for i in range(M+1) :
    A, B, C = map(int, input().split())
    edge.append([C, B, A])

edge.sort(key = lambda x : x[0])
parent = [_ for _ in range(N+1)]
zero = one = check_zero = check_one = 0

for value, x, y in edge :
    x = find(x)
    y = find(y)

    if x != y :
        if x > y:
            parent[x] = y
        else :
            parent[y] = x
        if value == 0 :
            check_zero += 1
edge.sort(key = lambda x :-x[0])
parent = [_ for _ in range(N+1)]
for value, x, y in edge :
    x = find(x)
    y = find(y)
    if x != y :
        if x > y :
            parent[x] = y
        else :
            parent[y] = x
        if value == 0 :
            check_one += 1
print(check_zero ** 2 - check_one**2)