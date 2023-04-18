from heapq import heappop, heappush
import sys
INF = sys.maxsize
def dijkstra(start_node) :
    heap = []
    dist = [INF for _ in range(N+1)]
    dist[start_node] = 0
    heappush(heap, (0, start_node))
    while heap :
        now_weight, now_end = heappop(heap)
        for next_node, next_weight in linked[now_end] :
            if next_weight + now_weight < dist[next_node] :
                dist[next_node] = next_weight + now_weight
                heappush(heap, (dist[next_node], next_node))
    return dist

input = sys.stdin.readline

N, M, X = map(int, input().split()) # N명의 학생 M개의 단방향 도로들.
linked = [[] for _ in range(N+1)]
for _ in range(M) :
    start, end , weight = map(int, input().split())
    linked[start].append((end, weight))

answer = [0 for _ in range(N+1)]
for now in range(1, N+1) :
    tmp = dijkstra(now)
    if now == X :
        for i in range(N+1) :
            answer[i] += (tmp[i] if tmp[i] != INF else 0)
    else :
        answer[now] +=  (tmp[X] if tmp[X] != INF else 0)

print(max(answer))