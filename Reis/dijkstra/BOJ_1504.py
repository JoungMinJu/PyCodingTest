import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 200000000

N, E = map(int, input().split()) # 정점의 개수 N 간선의 개수 E
linked = [[] for _ in range(N+1)]

for _ in range(E) :
    start, end, weight = map(int, input().split())
    linked[start].append((end, weight))
    linked[end].append((start, weight))

v1, v2 = map(int, input().split())

def dijkstra(start) :
    dp = [INF for _ in range(N+1)]
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap :
        now_weight, now_end = heappop(heap)
        if dp[now_end] < now_weight :
            continue
        for next_end, next_weight in linked[now_end] :
            next_value = now_weight + next_weight
            if dp[next_end] > next_value :
                heappush(heap, (next_value, next_end))
                dp[next_end] = next_value
    return dp

first = dijkstra(1)
second = dijkstra(v1)
third = dijkstra(v2)

cnt = min(first[v1] + second[v2] + third[N], first[v2] + third[v1] + second[N])
if cnt < INF :
    print(cnt)
else :
    print(-1)