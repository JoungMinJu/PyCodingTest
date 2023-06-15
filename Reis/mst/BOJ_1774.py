import sys

input = lambda: sys.stdin.readline().rstrip()


def get_dist(loc1, loc2):
    x1, y1, x2, y2 = loc1[0], loc1[1], loc2[0], loc2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def find(x) :
    if x != parent[x] :
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b) :
    a = find(a)
    b = find(b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b


N, M = map(int, input().split())  # 우주선들의 개수 / 통로의 개수

parent = list(range(N+1))
edges = [0] * (N+1)
for i in range(1, N+1) :
    edges[i] = list(map(int, input().split())) #  좌표 저장

for _ in range(M) :
    A, B = map(int, input().split())
    union(A, B)

possible = []
for i in range(1, len(edges)-1) :
    for j in range(i+1, len(edges)) :
        possible.append([get_dist(edges[i], edges[j]), i, j]) # 길이, 지점1, 지점2

possible.sort()
answer = 0

for p in possible :
    cost, x, y = p[0], p[1], p[2]
    if find(x) != find(y) :
        union(parent)
        answer += cost

print("{:.2f}".format(answer))
