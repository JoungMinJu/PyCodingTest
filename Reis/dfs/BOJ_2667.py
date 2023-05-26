import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

dR = [0, 0, 1,-1]
dC = [1,-1, 0,0]

def valid_range(row, col) :
    return 0 <= row < N and 0 <= col < N

def bfs(row, col) :
    count = 1
    que = deque()
    visited[row][col] = 1
    que.append([row, col])
    while que :
        now_row, now_col = que.popleft()
        for idx in range(4) :
            next_row, next_col = now_row + dR[idx], now_col + dC[idx]
            if not valid_range(next_row, next_col) :
                continue
            if board[next_row][next_col] and not visited[next_row][next_col] :
                visited[next_row][next_col] =1
                count += 1
                que.append([next_row, next_col])
    return count

N = int(input())
board = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
answer  = []
for row in range(N) :
    for col in range(N) :
        if board[row][col] and not visited[row][col] :
            answer.append(bfs(row,col))

answer.sort()
print(len(answer))
for a in answer :
    print(a)