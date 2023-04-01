# 후보를 담고 다 비교해야한다.
# 1. min_dist 구하고
#2. popleft 할 때마다 업데이트 해주기!
# 그리고 마지막에 sort()
# candidate에 아무것도 없으면 -1 return
# -> 예외 상황을 무조건 생각해보자


from collections import deque

def find_client(taxi):
    q = deque()
    q.append(taxi)
    visited = [[0] * N for _ in range(N)]
    min_distance = float('inf')
    candidate = []
    while q:
        y, x = q.popleft()
        if visited[y][x] > min_distance:
            break
        if [y, x] in clients_start:
            min_distance = visited[y][x]
            candidate.append([y, x])
        else:
            for d in range(4):
                ny, nx = y + dR[d], x + dC[d]
                if 0 <= ny < N and 0 <= nx < N and road[ny][nx] != 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])
    if candidate:
       candidate.sort()
       return visited[candidate[0][0]][candidate[0][1]], candidate[0][0], candidate[0][1]
    else:
       return -1, -1, -1


def go_to_dest(start, end): # 손님의 목적지로 가는 함수
    q = deque()
    q.append(start)
    visited = [[0] * N for _ in range(N)]
    while q:
        y, x = q.popleft()
        if [y, x] == end:
            break
        for d in range(4):
            ny, nx = y + dR[d], x + dC[d]
            if 0 <= ny < N and 0 <= nx < N and road[ny][nx] != 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny, nx])
    return visited[y][x], y, x


N, M, fuel = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
taxi_row, taxi_col = map(int, input().split())
taxi = [taxi_row - 1, taxi_col - 1]

clients_start = []
clients_end = []
for _ in range(M) :
    s_row, s_col, d_row, d_col = map(int, input().split())
    clients_start.append([s_row-1, s_col-1])
    clients_end.append([d_row-1, d_col-1])

dR = [1, 0, -1, 0]
dC = [0, 1, 0, -1]

for _ in range(M) :
    distance, client_row, client_col = find_client(taxi)
    if distance == -1 or fuel - distance < 0 :
        fuel = -1
        break
    fuel -= distance
    idx = clients_start.index([client_row, client_col]) # 해당 손님 인덱스 찾고
    clients_start[idx] = [-1, -1]
    dest_row, dest_col  = clients_end[idx]
    distance2, d_row, d_col = go_to_dest([client_row, client_col], [dest_row, dest_col])
    if [d_row, d_col] != [dest_row, dest_col] or fuel - distance2 < 0 :
        fuel = -1
        break
    fuel += distance2
    taxi = [d_row, d_col]
print(fuel)