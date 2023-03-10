from heapq import heappush,heappop
import sys
input = lambda : sys.stdin.readline().rstrip()

INF = 10**9
N, M = map(int, input().split())

dist = [INF for _ in range(N+1)]
link = [[] for _ in range(N+1)]

for _ in range(M) :
    start, end, weight = map(int, input().split())
    link[start].append((end, weight))
    link[end].append((start, weight))

heap = []
dist[1] = 0
parent = [0] * (N+1)
heappush(heap, (0, 1)) # 무게, 노드

while heap :
    now_weight, now_end =heappop(heap)
    for (next_end, next_weight) in link[now_end] :
        if dist[now_end] < now_weight :
            continue
        if (now_weight + next_weight) < dist[next_end] :
            parent[next_end] = now_end
            dist[next_end] = now_weight + next_weight
            heappush(heap, (dist[next_end], next_end))


print(N-1)
for i in range(2, N+1) :
    print(i, parent[i])