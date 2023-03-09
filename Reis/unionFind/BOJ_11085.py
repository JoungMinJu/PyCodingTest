from heapq import heappush, heappop

def find(x) :
    if parent[x] == x :
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b) :
    a = find(a)
    b = find(b)
    if a != b :
        if a < b :
            parent[b] = a
        else :
            parent[a] = b

P, W = map(int, input().split())
C, V = map(int, input().split())

parent = list(range(P))
graph = []

for i in range(W):
     start, end, width = map(int, input().split())
     heappush(graph, (-width, start, end))

answer = 0
while graph :
    width, start, end = heappop(graph)
    width = -width

    union(start, end)

    if find(C) == find(V) :
        answer = width
        break
print(answer)