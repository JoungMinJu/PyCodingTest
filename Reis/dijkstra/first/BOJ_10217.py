# 최대 M원
import sys
from heapq import heappush, heappop

input = lambda : sys.stdin.readline().rstrip()
INF = float("inf")

test_size = int(input())
for test in range(test_size) :
    N, cost, M = map(int, input().split()) # 공항의 수, 총 지원 비용, 티켓 정보의 수
    dp = [[INF] * N for _ in range(cost+1)] # 열 = 노드 / 행 = 비용
    graph = [[] for _ in range(N)]

    for i in range(M) :
        U, V, C, D = map(int, input().split()) # 도착, 출발, 비용, 시간
        graph[U-1].append((V-1, C, D)) # 도착점, 비용, 시간 저장
    heap = [(0, 0, 0)] # 거리, 비용, 노드
    while heap :
        now_dist, now_cost, now_node = heappop(heap)
        if now_dist > dp[now_cost][now_node] :
            continue
        for to_node, to_cost, to_dist in graph[now_node] :
            tmp_dist = now_dist + to_dist
            tmp_cost = now_cost + to_cost
            if tmp_cost <= cost and tmp_dist < dp[tmp_cost][to_node]:
                # 더 높은 cost를 투자할 때의 가중치도 초기화 해주기
                for c in range(tmp_cost, cost+1) :
                    if dp[c][to_node] > tmp_dist :
                        dp[c][to_node] = tmp_dist
                    else:
                        break
                heappush(heap, (tmp_dist, tmp_cost, to_node))

    print(dp[cost][N-1] if dp[cost][N-1] != INF else "Poor KCM")

