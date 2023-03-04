from collections import deque
import sys
input = sys.stdin.readline

dR = [1, 2, 2, 1, -1, -2, -2, -1]
dC = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs (row, col) :
    global end_row, end_col, L
    que = deque()
    que.append((row, col))
    visited[row][col] = True

    while que :
        now_row, now_col = que.popleft()
        if (now_row, now_col) == (end_row, end_col) :
            return
        for idx in range(8) :
            next_row = now_row + dR[idx]
            next_col = now_col + dC[idx]
            if next_row not in range(L) or next_col not in range(L) :
                continue
            if not visited[next_row][next_col] :
                visited[next_row][next_col] = True
                graph[next_row][next_col] = graph[now_row][now_col] + 1
                que.append((next_row, next_col))

test_size = int(input())

for test in range(test_size) :
    L = int(input()) # 체스판 한 변의 길이
    graph = [[0] * L for _ in range(L)]
    visited = [[False] * L for _ in range(L)]
    start_row, start_col = map(int, input().split())
    end_row, end_col = map(int, input().split())
    bfs(start_row, start_col)
    print(graph[end_row][end_col])