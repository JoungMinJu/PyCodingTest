import sys
from collections import deque
input = sys.stdin.readline

dR = [-1, 1, 0, 0]
dC = [0, 0, 1, -1]

def bfs() :
    global answer, unripe_count

    while que :
        if unripe_count == 0:
            return answer
        que_size = len(que)
        answer += 1
        for count in range(que_size) :
            now_row, now_col = que.popleft()
            visited[now_row][now_col] = True
            for idx in range(4) :
                next_row = now_row + dR[idx]
                next_col = now_col + dC[idx]
                if next_row not in range(N) or next_col not in range(M) or visited[next_row][next_col] :
                    continue
                if graph[next_row][next_col] == 0 :
                    que.append((next_row, next_col))
                    graph[next_row][next_col] = 1
                    unripe_count -= 1
    return -1


M, N = map(int, input().split()) # 열 행
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * (M+1) for _ in range(N)]
unripe_count = 0
answer = 0
que = deque()

for row in range(N):
    for col in range(M) :
        if graph[row][col] == 0 :
            unripe_count += 1
        elif graph[row][col] == 1:
            que.append((row, col))

if len(que) == 0 and len(que) > 0:
    print(0)
else :
    print(bfs())