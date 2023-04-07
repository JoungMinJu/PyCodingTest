import sys
from heapq import heappop, heappush

def dijkstra(start) :
    dp = [INF] * (N+1)
    dp[start] = 0 # 처음 시작점
    heap = []
    heappush(heap, [0, start])
    while heap :
        w, c = heappop(heap)
        for next_n, next_w in s[c] :
            wei = w + next_w
            if dp[next_n] > wei :
                dp[next_n] = wei
                heappush(heap, [wei, next_n])
    return dp

N, E = map(int, input().split())
S = [[] for _ in range(N+1)] #정점 개수
INF = sys.maxsize

for _ in range(E) :
    start, end, dist = map(int, input().split())
    S[start].append([end, dist])
    S[end].append([start, dist])
v1, v2 = map(int, input().split())

one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
ctn = min(one[v1]+v1_[v2]+v2_[N], one[v2] + v2_[v1] + v1_[N])
