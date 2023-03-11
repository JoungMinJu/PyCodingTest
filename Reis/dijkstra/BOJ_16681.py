import sys
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 6


def dijkstra(start):
    heap = []
    heappush(heap, (0, start))
    dist = [INF for _ in range(N + 1)]
    dist[start] = 0

    while heap:
        now_weight, now_node = heappop(heap)
        for next_node, next_weight in link[now_node]:
            if dist[next_node] < next_weight:
                continue
            if dist[next_node] > now_weight + next_weight and heights[now_node] <= heights[next_node]:
                dist[next_node] = now_weight + next_weight
                heappush(heap, (dist[next_node], next_node))
    return dist


N, M, D, E = map(int, input().split())
# 지도에 표시된 지점 개수 N
# 지점을 잇는 경로의 개수 M
# 거리 비례 체력 소모량 D
# 높이 비례 성취감 획득량 E

heights = [0] + list(map(int, input().split()))
link = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, length = map(int, input().split())
    link[start].append((end, length))
    link[end].append((start, length))

start_dist = dijkstra(1)
end_dist = dijkstra(N)

answer = -float(INF)
for i in range(2, N):
    answer = max(answer, heights[i] * E - (start_dist[i] + end_dist[i]) * D)

print(answer if answer != -INF else "Impossible")
