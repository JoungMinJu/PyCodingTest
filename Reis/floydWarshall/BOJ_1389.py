import sys
INF = float('inf')
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
dist = [[INF] * (N+1) for _ in range(N+1)]
for person in range(1, N+1) :
    dist[person][person] = 0
for _ in range(M) :
    A, B = map(int, input().split())
    dist[A][B] = 1
    dist[B][A] = 1

# 플로이드 워셜 진행
for middle in range(1, N+1) :
    for start in range(1, N+1) :
        for end in range(1, N+1) :
            dist[start][end] = min(dist[start][end], dist[start][middle] + dist[middle][end])

answer = 0
min_value = INF
for person in range(1, N+1) :
    now_value = 0
    for target in range(1, N+1) :
        if person  != target :
            now_value += dist[person][target]
    if min_value > now_value :
        min_value = now_value
        answer = person
print(answer)