from collections import deque

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

def valid_range(row, col) :
    return 0 <= row < N and 0 <= col < N

def find_client(start_row, start_col) :
    que = deque()
    que.append([start_row, start_col])
    visited = [[0] * N for _ in range(N)]
    visited[start_row][start_col] = 1
    for idx, client in enumerate(clients) :
        c_r, c_c, d_r, d_c = client
        if [c_r, c_c] == [start_row, start_col] :
            return 0, idx
        visited[c_r][c_c] = -(idx+1)
    candidates = []
    flag = 0
    cnt = 0
    while que :
        if flag : # 성공했다면
            break
        size = len(que)
        cnt += 1
        for _ in range(size) :
            now_row, now_col = que.popleft()
            for md in range(4) :
                next_row, next_col = now_row + dR[md], now_col + dC[md]
                if not valid_range(next_row, next_col) or board[next_row][next_col]:
                    continue
                if visited[next_row][next_col] <= 0:
                    if visited[next_row][next_col] < 0 :
                        flag = 1
                        candidates.append([next_row, next_col, cnt]) # 행 열 cnt
                    else :
                        visited[next_row][next_col] = 1
                        que.append([next_row, next_col])
    candidates.sort()
    if len(candidates) == 0 :
        return -1, -1
    result_row, result_col, result_cnt = candidates[0]
    result_id  = (visited[result_row][result_col] * -1) -1
    return result_cnt, result_id

def find_dest(start_row, start_col, dest_row, dest_col) :
    que = deque()
    que.append([start_row, start_col])
    visited = [[0] * N for _ in range(N)]
    visited[start_row][start_col] = 1
    cnt = 0
    while que :
        size = len(que)
        cnt += 1
        for _ in range(size) :
            now_row, now_col = que.popleft()
            for idx in range(4) :
                next_row, next_col = now_row + dR[idx], now_col + dC[idx]
                if not valid_range(next_row, next_col) or board[next_row][next_col] :
                    continue
                if not visited[next_row][next_col] :
                    if [next_row, next_col] == [dest_row, dest_col] :
                        return cnt
                    visited[next_row][next_col] = 1
                    que.append([next_row, next_col])
    return -1



N, M, oil = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
t_row, t_col = map(int, input().split()) # -1 필요
t_row, t_col = t_row - 1, t_col - 1
clients = []
for _ in range(M) :
    s_r, s_c, d_r, d_c = map(int, input().split())
    s_r, s_c, d_r, d_c = s_r -1, s_c -1, d_r -1, d_c -1
    clients.append([s_r, s_c, d_r, d_c])

while True :
    # 1. 내 위치에서 출발지까지 젤 가까운 승객 찾기
    used_oil, client_id = find_client(t_row, t_col)
    if [used_oil, client_id] == [-1, -1] :
        print(-1)
        break
    # 해당 승객 가져오기
    client_row, client_col, dest_row, dest_col = clients.pop(client_id)
    oil -= used_oil
    if oil < 0 :
        print(-1)
        break
    # -> 승객 위치 = 택시 위치.
    t_row, t_col = client_row, client_col
    # 2. 내 위치에서 목적지까지 이동
    used_oil = find_dest(t_row, t_col, dest_row, dest_col)
    if used_oil == -1 :
        print(-1)
        break
    # -> 간 오일 빼보기
    if oil - used_oil < 0 :
        print(-1)
        break
    oil += used_oil
    t_row, t_col = dest_row, dest_col
    if len(clients)== 0:
        print(oil)
        break
