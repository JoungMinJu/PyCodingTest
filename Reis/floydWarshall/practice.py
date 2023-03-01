INF = int(1e9) # 10억

n = int(input()) # 노드 개수
m = int(input()) # 간선 개수
graph = [[INF] * (n+1) for _ in range(n+1)]

# 본인 -> 본인 경로는 0으로 초기화
for start in range(1, n+1) :
    for end in range(1, n+1):
        if start == end :
            graph[start][end] = 0

# 경로 입력 받고 초기화
for _ in range(m):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight

# 점화식에 따른 플로이드-워셜 알고리즘
for middle in range(1, n+1): # 라운드
    for start in range(1, n+1) :
        for end in range(1, n+1) :
            graph[start][end] = min(graph[start][end], graph[start][middle] + graph[middle][end])

# 결과 출력
for start in range(1, n+1) :
    for end in range(1, n+1) :
        if graph[start][end] == INF :
            print("INFINITY", end= " ")
        else :
            print(graph[start][end], end= " ")
    print()