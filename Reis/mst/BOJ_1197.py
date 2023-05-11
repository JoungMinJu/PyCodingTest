import sys
input = lambda : sys.stdin.readline()

def find(x) :
    if parents[x] != x :
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b) :
    a = find(a)
    b = find(b)
    if a < b :
        parents[b] = a
    else :
        parents[a] = b

def is_same(a, b) :
    return find(a) == find(b)

V, E = map(int, input().split())
# 사이클 없이 모든 정점이 연결되어있는 그래프. 간선의 개수 V-1개가 됨.
# 1. 모든 간선 가중치 기준 오름차순 정렬
# 2. 가중치 젤 낮은 애부터 순회하면서
# 3. 이 간선이 추가된다면 사이클이 발생시키는지 확인한다

edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key = lambda x : x[2])  # cost순 오름차순

parents = [i for i in range(v+1)]

answer = 0
for a, b, cost in edges :
    if not is_same(a, b) : # 사이클 없으면
        union(a, b)
        answer += cost
print(answer)

