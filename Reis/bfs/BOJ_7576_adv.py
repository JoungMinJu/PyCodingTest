from collections import deque

M, N = map(int, input().split())
graph = []
que = deque()

for i in range(N) :
    graph.append(list(map(int, input().split())))

    for j in range(M):
        if graph[i][j] == 1 :
            que.append([i,j])

dR = [-1, 1, 0, 0]
dC = [0, 0, 1, -1]

def bfs() :
    while que :
        row, col = que.popleft()
        for i in range(4) :
            next_row = row + dR[i]
            next_col = col + dC[i]
            if 0 <= next_row < N and 0 <= next_col < M and graph[next_row][next_col] == 0:
                que.append([next_row, next_col])
                graph[next_row][next_col] = graph[row][col] +1

bfs()
answer = 0

for i in graph :
    for j in i :
        if j == 0 :
            print(-1)
            exit(0)
    answer = max(answer,  max(i))
print(answer-1)