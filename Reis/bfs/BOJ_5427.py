from collections import deque
import sys

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

def bfs(dq) :
    while dq :
        row, col = dq.popleft()
        chk = visited[row][col]
        for i in range(4) :
            next_row = row + dR[i];
            next_col = col + dC[i];

            if next_row < 0 or next_row >=h or next_col < 0 or next_col >= w :
                if chk != -2: # 불 아니면
                    return visited[row][col] + 1
            else :
                if visited[next_row][next_col] == -1 and (building[next_row][next_col] == '.' or building[next_row][next_col] == '@') : # 방문 안했는데 빈 칸이거나 시작점(빈칸) 이면
                    if chk == -2: # 내가 불이면
                        visited[next_row][next_col] = -2
                    else :
                        visited[next_row][next_col] = visited[row][col] + 1
                    dq.append((next_row, next_col))
    return "IMPOSSIBLE"


test_size = int(sys.stdin.readline()) # 반복문으로 여러 줄 입력 받을 때는 이거 사용하기

for test in range(test_size) :
    w, h = map(int, sys.stdin.readline().split(" "))
    building = []
    start = []
    fire = []
    visited = [[-1] * w for _ in range(h)]

    for row in range(h) :
        tmp = sys.stdin.readline()
        building.append(tmp)
        for col in range(w) :
            if tmp[col] == '*' :
                fire.append((row, col))
                visited[row][col] = -2
            elif tmp[col] == '@' :
                start.append((row, col))
                visited[row][col] = 0

    dq = deque()
    dq.extend(fire)
    dq.extend(start)

    print(bfs(dq))
