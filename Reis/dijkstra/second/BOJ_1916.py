from heapq import heappop, heappush
import sys

input = lambda : sys.stdin.readline().rstrip()
INF = float('inf')

def dijkstra(start) :
    que = []
    dist[start] =0
    heappush(que, [0, start])
    while que :
        now_weight, now_end = heappop(que)
        if dist[now_end] < now_weight :
            continue #끊어주기
        for link_end, link_weight in linked[now_end] :
            if dist[link_end] > link_weight + now_weight:
                dist[link_end] = link_weight + now_weight
                heappush(que, [dist[link_end], link_end])

# 1~N번 도시
N = int(input())
M = int(input())

linked = [list() for _ in range(N+1)]
dist = [INF] * (N+1)

for _ in range(M) :
    start, end, weight = map(int, input().split())
    linked[start].append((end, weight))

final_start, final_end = map(int, input().split())
dijkstra(final_start)
print(dist[final_end])