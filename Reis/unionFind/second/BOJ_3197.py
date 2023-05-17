'''
2차원 좌표 union-find에선 rank 제도 도입
'''
import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

def valid_range(row, col) :
    return 0 <= row < R and 0 <= col < C

def find(v) :
    if v == root[v[0]][v[1]] :
        return v
    root[v[0]][v[1]] = find(root[v[0]][v[1]])
    return root[v[0]][v[1]]

def union(v1, v2) :
    r1 =find(v1)
    r2 = find(v2)

    if rank[r1[0]][r1[1]] > rank[r2[0]][r2[1]]:
        root[r2[0]][r2[1]] = r1
    elif rank[r1[0]][r1[1]] < rank[r2[0]][r2[1]]:
        root[r1[0]][r1[1]] = r2
    else:
        root[r2[0]][r2[1]] = r1
        rank[r1[0]][r1[1]] += 1

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
root = [[(row, col) for col in range(C)] for row in range(R)] # 부모!! 저장
rank = [[0] * C for _ in range(R)] # union 최적화
visited = [[0] * C for _ in range(R)]
swan = [] # 백조가 위치한 행과 열

for row in range(R) :
    for col in range(C) :
        if board[row][col] == "L" :
            swan.append([row, col])
            board[row][col] = '.' # 물으로 바꾸기
            if len(swan) == 2 :
                break

melt = deque() # 인접한 빙판 저장
for row in range(R) :
    for col in range(C) :
        if not visited[row][col] and board[row][col] == "." : # 방문 안 한 물이면
            que = deque()
            que.append([row, col])
            visited[row][col] = 1
            while que :
                now_row, now_col = que.popleft()
                root[now_row][now_col] = [row, col] # 루트 지정해주기
                for idx in range(4) :
                    next_row, next_col = now_row + dR[idx], now_col + dC[idx]
                    if valid_range(next_row, next_col) and not visited[next_row][next_col] :
                        if board[next_row][next_col] == ".":
                            visited[next_row][next_col] = 1
                            que.append([next_row, next_col])
                        elif board[next_row][next_col] == "X" : # 빙하면
                            visited[next_row][next_col] = 1
                            melt.append([next_row, next_col])

day = 0
while find(swan[0]) != find(swan[1]) :
    tmp = deque() # 새로 녹이는 놈 인접한 빙판 저장
    while melt : # 인접한 빙판 녹이기
        row, col = melt.popleft()
        board[row][col] = "." # 녹여버리고
        merge_point =[] # 새로 녹은 놈 근처에 있는 물 저장
        for idx in range(4) :
            next_row, next_col = row + dR[idx], col + dC[idx]
            if not valid_range(next_row, next_col) :
                continue
            if not visited[next_row][next_col] and board[next_row][next_col] == "X" :
                visited[next_row][next_col] = 1
                tmp.append([next_row, next_col])
            elif board[next_row][next_col] == '.' :
                merge_point.append([next_row, next_col])
        for rt in merge_point :
            if find(rt) != find([row, col]) :
                union(rt, [row, col])
    melt = tmp
    day += 1
print(day)
