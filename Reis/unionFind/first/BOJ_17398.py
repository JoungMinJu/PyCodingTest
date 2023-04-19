import sys
sys.setrecursionlimit(10**9)

input = lambda : sys.stdin.readline().rstrip()

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y) :
    x = find(x)
    y = find(y)
    if x < y :
        parent[y] = x
        cnt[x] += cnt[y]
    elif x > y :
        parent[x] = y
        cnt[y] += cnt[x]

N, M, Q = map(int, input().split())
parent = [i for i in range(N + 1)]
cnt = {i:1 for i in range(1, N+1)}

linked = [[0, 0]]
for i in range(M) :
    a, b = map(int, input().split())
    linked.append([a, b])

dis = []
check = [1] * (M+1)
for i in range(Q) :
    d = int(input())
    dis.append(d)
    check[d] = 0

for i in range(1, M+1) :
    if check[i] : # 없어질 링크 아니면
        union(linked[i][0], linked[i][1])

pay = 0
for i in range(Q-1, -1, -1) :
    # 거꾸로부터 줄이기
    x = dis[i]
    a, b = linked[x][0], linked[x][1]
    p_a = find(a)
    p_b = find(b)
    if p_a != p_b :
        pay += (cnt[p_a] * cnt[p_b])
    union(a,b)

print(pay)