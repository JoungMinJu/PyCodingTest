import sys
from collections import deque

r, c = map(int, input().split())

arr = []
q = deque()

for _ in range(r):
    arr.append(list(sys.stdin.readline().rstrip()))

waterMap = [[-1] * c for _ in range(r)]
beaverMap = [[-1] * c for _ in range(r)]
start = []
end = []

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'D':
            end = [i, j]
        elif arr[i][j] == 'S':
            start = [i, j]
            beaverMap[i][j] = 0
            arr[i][j] = '.'
        elif arr[i][j] == '*':
            q.append([i, j])
            waterMap[i][j] = 0
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 물이 갈 수 있는 최단 경로를 먼저 waterMap 에 표시해줍니다.
while q:
    x, y = q.popleft()
    for i in range(4):
        dx = x + dir[i][0]
        dy = y + dir[i][1]
        if 0 <= dx < r and 0 <= dy < c and arr[dx][dy] == '.' and waterMap[dx][dy] == -1:
            waterMap[dx][dy] = waterMap[x][y] + 1
            q.append([dx, dy])


# 고슴도치가 갈 수 있는 곳을 waterMap과 비교해 waterMap보다 작으면 갈 수 있게 해줍니다.
# 단, 동시에 물과 고슴도치가 도착하는 경우도 이동할 수 없으므로 +1로 비교해줍니다.
q.append(start)
while q:
    x, y = q.popleft()
    for i in range(4):
        dx = x + dir[i][0]
        dy = y + dir[i][1]
        if 0 <= dx < r and 0 <= dy < c and arr[dx][dy] in '.D' and beaverMap[dx][dy] == -1:
            if beaverMap[x][y] + 1 < waterMap[dx][dy] or waterMap[dx][dy] == -1:
                beaverMap[dx][dy] = beaverMap[x][y] + 1
                q.append([dx, dy])


# 고슴도치가 갈수 없는 경우 KAKTUS를 표시
if beaverMap[end[0]][end[1]] == -1:
    print('KAKTUS')
else:
    print(beaverMap[end[0]][end[1]])