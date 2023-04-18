from heapq import heappop, heappush
import sys

input = lambda : sys.stdin.readline().rstrip()
INF = float('inf')

def dijkstra(start) :
    global dist
    dist[start] = 0
    hq = []
    heappush(hq, [0, start])
    while hq :
        now_weight, now_start  = heappop(hq)
        for next_end, next_weight in linked[now_start] :
            total_weight  = next_weight + now_weight
            if dist[next_end] > total_weight :
                dist[next_end] = total_weight
                heappush(hq, [total_weight, next_end])


V, E = map(int, input().split()) # 정점 개수, 간선 개수
start = int(input())

linked = [list() for _ in range(V+1)]
for _ in range(E) :
    u, v, w = map(int, input().split())
    linked[u].append([v,w])

dist = [INF] * (V+1)
dijkstra(start)
for i in range(1, V+1) :
    print(dist[i] if dist[i] != INF else "INF")