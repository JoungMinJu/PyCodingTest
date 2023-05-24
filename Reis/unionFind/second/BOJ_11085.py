import sys

input = lambda: sys.stdin.readline().rstrip()

def find(v) :
    if parent[v] != v :
        parent[v] = find(parent[v])
    return parent[v]

def union(v, w) :
    v = find(v)
    w = find(w)
    if v > w :
        parent[w] = v
    elif v < w :
        parent[v] = w

''' 
간선을 w순으로 정렬 -> w가 큰 간선부터 union 연산을 한다.
'''
P, W = map(int, input().split())
C, V = map(int, input().split())

parent = [i for i in range(P)]

links = [list(map(int, input().split())) for _ in range(W)]
links.sort(key = lambda x : -x[2])
for start, end, weight in links :
    union(start, end)
    if find(C) == find(V) :
        print(weight)
        break