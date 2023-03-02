import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

linked = [[] for _ in range(N+1)]
dist = [INF] * (N+1)

for _ in range(M):
    start, end, weight = map(int, input().split())
    linked[start].append((end, weight))

start, end = map(int, input().split())

def dijkstra(start) :
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start)) # 가중치, 도착지점
    while pq :
        now_weight, now_end = heapq.heappop(pq)
        if dist[now_end] < now_weight :
            continue
        for next_end, next_weight in linked[now_end]:
            next_value = now_weight + next_weight
            if dist[next_end] > next_value:
                heapq.heappush(pq, (next_value, next_end))
                dist[next_end] = next_value

dijkstra(start)
print(dist[end])
