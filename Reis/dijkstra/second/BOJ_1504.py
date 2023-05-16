import sys
from heapq import heappush, heappop

input = lambda : sys.stdin.readline().rstrip()
INF = float('inf')

def dijkstra(start) :
    dist = [INF] * (N+1)
    dist[start] = 0
    pq = []
    heappush(pq, [0, start])
    while pq :
        now_cost, now_node = heappop(pq)
        for next_node, next_cost in links[now_node] :
            if dist[next_node] < next_cost :
                continue
            if dist[next_node] > now_cost + next_cost :
                dist[next_node] = now_cost + next_cost
                heappush(pq, [dist[next_node], next_node])
    return dist

# 임의로 주어진 두 정점은 반드시 통과하기
N, E = map(int, input().split())
links = [list() for _ in range(N+1)] # 정점별 link 정보
for _ in range(E) :
    start, end, cost = map(int, input().split())
    links[start].append([end, cost])
    links[end].append([start, cost])

V1, V2 = map(int, input().split())

first_dist = dijkstra(1)
v1_dist = dijkstra(V1)
v2_dist = dijkstra(V2)

first_v1_v2_end = first_dist[V1] + v1_dist[V2] + v2_dist[N]
first_v2_v1_end = first_dist[V2] + v2_dist[V1] + v1_dist[N]

if first_v1_v2_end == INF and first_v2_v1_end == INF:
    print(-1)
else :
    print(min(first_v1_v2_end, first_v2_v1_end))
