from heapq import heappop, heappush
import sys

def find_parent(x) :
    if x != parent[x] :
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x,y) :
    x = find_parent(x)
    y = find_parent(y)
    if x < y :
        parent[y] = x
        child_num[x] += child_num[y]
    else :
        parent[x] = y
        child_num[y] += child_num[x]

def find_child_num(x) :
    if parent[x] != x :
        return find_child_num(parent[x])
    return child_num[x]

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
parent = [-1] * (N+1)
child_num = [1] * (N+1) # 자신 포함 자식의 개수
for i in range(1, N+1) :
    parent[i] = i
edge = []
total = 0 # 가중치 총합
for _ in range(M) :
    x, y, w = map(int, input().split())
    heappush(edge, (-w, x, y)) # 가중치 높은 순 정렬
    total += w

answer = 0
current_total = 0
for _ in range(M) :
    w, x, y = heappop(edge)
    if find_parent(x) != find_parent(y) : #연결 안되어 있으면
        # (지금 cost)가 (집합 개수 * 집합 개수) 만큼 생긴다는 의미
        answer += find_child_num(x) * find_child_num(y) * (total - current_total)
        union_parent(x,y)
    current_total -= w
print(answer % 10**9)
