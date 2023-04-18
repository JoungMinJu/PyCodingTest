import sys
from heapq import heappop, heappush
from collections import deque, defaultdict
import heapq

input = lambda: sys.stdin.readline()
INF = float("inf")

def dijkstra(start_node, edges) :
    heap = []
    dist = [INF for _ in range(N+1)]
    dist[start_node] = 0
    heappush(heap, (0, start_node))
    while heap :
        now_weight, now_end = heappop(heap)
        for next_node, next_weight in edges[now_end] :
            if next_weight + now_weight < dist[next_node] and edge_check[now_end][next_node]:
                dist[next_node] = next_weight + now_weight
                heappush(heap, (dist[next_node], next_node))
    return dist


while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    start, end = map(int, input().split())
    edge = [[] for _ in range(N)]
    edge_reverse = [[] for _ in range(N)]
    edge_check = [[False] * N for _ in range(N)]

    for _ in range(M) :
        U, V, P = map(int, input().split())
        edge[U].append((V, P))
        edge_reverse[V].append((U, P))
        edge_check[U][V] = True

    dist1 = dijkstra(start,  edge)
    if dist1[end] == INF :
        print(-1)
        continue
    shortest  = dist1[end]

    # 최단 경로 제거
    que = deque([(0, end)])
    while que :
        cur_dist, cur_node = que.popleft()
        for to_node, to_dist in edge_reverse[cur_node]:
            d = cur_dist + to_dist
            if d + dist1[to_node] == shortest :
                if edge_check[to_node][cur_node] :
                    edge_check[to_node][cur_node] = False
                    que.append((d, to_node))

    ans = dijkstra(start,  edge)
    print(ans[end] if ans[end] != INF else -1)
