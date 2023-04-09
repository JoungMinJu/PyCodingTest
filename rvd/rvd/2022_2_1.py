from collections import deque

N, M = map(int, input().split())

dR = [0, -1, 0, 0, 1]
dC = [0, 0, -1, 1, 0]

def valid_range(row, col) :
    return 0 <= row < N and 0 <= col < N

def bfs(start_row,start_col, end_row, end_col) :
    que = deque()
    visited = [[list() for _ in range(N)] for _ in range(N)]
    que.append([start_row, start_col])
    visited[start_row][start_col] =  [-1] # 빈 값
    while que :
        size = len(que)
        for _ in range(size) :
            now_row, now_col = que.popleft()
            for idx in range(1,5) :
                next_row, next_col = now_row + dR[idx], now_col + dC[idx]
                if not valid_range(next_row, next_col) :
                    continue
                if len(visited[next_row][next_col]) == 0 and board[next_row][next_col] != -1 :
                    if visited[now_row][now_col] != [-1] :
                        visited[next_row][next_col] = visited[now_row][now_col] + [[next_row,next_col]]
                    else :
                        visited[next_row][next_col] = [[next_row,next_col]]
                    if [next_row, next_col] == [end_row, end_col] :
                        return visited[next_row][next_col]
                    else :
                        que.append([next_row, next_col])
    return [] # 도달 못하면 빈 리스트

def find_camp(start_row, start_col) :
    que = deque()
    visited = [[0] * N for _ in range(N)]
    que.append([start_row,start_col])
    visited[start_row][start_col] = 1
    candidates = []
    while que :
        size = len(que)
        if len(candidates) > 0 :
            candidates.sort()
            return candidates[0]
        for _ in range(size) :
            now_row, now_col = que.popleft()
            for idx in range(1,5) :
                next_row, next_col = now_row + dR[idx], now_col + dC[idx]
                if not valid_range(next_row, next_col):
                    continue
                if not visited[next_row][next_col] and board[next_row][next_col] != -1 :
                    if board[next_row][next_col] == 1 :
                        candidates.append([next_row, next_col])
                    else :
                        visited[next_row][next_col] = 1
                        que.append([next_row, next_col])
    return -1, -1 # 도달 못하면

board = [list(map(int, input().split())) for _ in range(N)]
person = [[-1, -1]]
for _ in range(M) :
    dest_row, dest_col = map(int, input().split())
    person.append([dest_row-1, dest_col-1])

in_person = deque() # 인덱스 넣어주기
person_route = [list() for _ in range(M+1)]
tmp_cannot_move = deque()
cnt_person = M
t = 1
while True :
    # 1. 이동 -> 격자에 있는 사람들 정보, 못 지나다니는 칸
    size = len(in_person)
    for _ in range(size) :
        person_idx, person_row, person_col = in_person.popleft()
        dest_row, dest_col = person[person_idx]
        if len(person_route[person_idx]) == 0 :
            person_route[person_idx] = bfs(person_row, person_col, dest_row,dest_col)
        while True :
            next_row, next_col = person_route[person_idx].pop(0)
            if board[next_row][next_col] != -1 :
                if [next_row, next_col] == [dest_row, dest_col]:
                    tmp_cannot_move.append([next_row, next_col])
                    cnt_person -= 1
                else :
                    in_person.append([person_idx,next_row,next_col])
                break
            person_route[person_idx] = bfs(person_row, person_col,dest_row, dest_col)
    if t <= M :
        dest_row,dest_col = person[t]
        base_row, base_col = find_camp(dest_row, dest_col)
        tmp_cannot_move.append([base_row, base_col])
        in_person.append([t, base_row, base_col])
    while tmp_cannot_move :
        row, col = tmp_cannot_move.popleft()
        board[row][col] = -1
    if cnt_person <= 0 :
        break
    t += 1

print(t)