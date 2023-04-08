from collections import defaultdict, deque

dR = [0, -1, 1, 0, 0]
dC = [0, 0, 0, -1, 1]

move_dR = [0, 1, 0, -1]
move_dC = [-1, 0, 1, 0]


def valid_range(row, col):
    return 0 <= row < N and 0 <= col < N

def update_indexes(now_row, now_col):
    indexes = []
    max_len = 1
    idx = 0
    flag = 1
    while True :
        for _ in range(max_len):
            next_row, next_col = now_row + move_dR[idx%4], now_col + move_dC[idx%4]
            if not valid_range(next_row, next_col) :
                flag = 0
                break
            indexes.append([next_row, next_col])
            now_row, now_col = next_row, next_col
        if not flag  :
            break
        idx += 1
        if idx % 2 == 0:
            max_len += 1
    return indexes


def destroy(d, s):
    for length in range(1, s+1) :
        next_row, next_col = shark_row + dR[d] * length, shark_col + dC[d] * length
        if not valid_range(next_row, next_col) :
            break
        A[next_row][next_col] = 0

def move():
    now_idx = 0
    next_idx = 1
    while True :
        if next_idx >= (N*N) -1 :
            break
        now_row, now_col = indexes[now_idx]
        next_row, next_col  = indexes[next_idx]
        if not valid_range(next_row, next_col) :
            break
        next_num = A[next_row][next_col]
        if next_num : # 0이 아니면
            A[next_row][next_col] = 0
            if A[now_row][now_col] : # 나도 있으면
                tmp_row,tmp_col = indexes[now_idx+1]
                A[tmp_row][tmp_col] = next_num
                now_idx += 1
            else :
                A[now_row][now_col] = next_num
        next_idx += 1

def update():
    answer = [] # 넣기
    now_idx = 0
    now_row, now_col = indexes[now_idx]
    before_num = A[now_row][now_col]
    cnt = 1
    while True :
        now_idx += 1
        if now_idx >= N*N-1 :
            break
        now_row, now_col = indexes[now_idx]
        now_num = A[now_row][now_col]
        if before_num != now_num :
            answer.append([cnt, before_num])
            before_num = now_num
            cnt = 1
        else :
            cnt += 1
    return answer

def bomb() : # 폭파
    answer = deque()
    now_idx = 0
    now_row, now_col = indexes[now_idx]
    answer.append([now_row, now_col])
    before_num = A[now_row][now_col]
    cnt = 1
    flag = 0
    while True :
        now_idx += 1
        if now_idx >= N*N -1 :
            break
        now_row, now_col = indexes[now_idx]
        now_num = A[now_row][now_col]
        if before_num != now_num :
            if cnt >= 4 :
                flag = 1
                while answer :
                    row, col = answer.popleft()
                    answer_cnt[A[row][col]] += 1
                    A[row][col] = 0
            before_num = now_num
            cnt = 1
            if len(answer) >= 1 :
                answer = deque()
                answer.append([now_row,now_col])
        else :
            cnt += 1
            answer.append([now_row, now_col])
    return flag

def update_A(tmp_answer) :
    idx = 0
    for num1, num2 in tmp_answer :
        if idx >= N*N-1 :
            return
        now_row, now_col = indexes[idx]
        A[now_row][now_col] = num1
        idx += 1
        if idx >= N*N-1 :
            return
        now_row, now_col = indexes[idx]
        A[now_row][now_col] = num2
        idx += 1
    while idx < N*N-1 :
        now_row, now_col = indexes[idx]
        A[now_row][now_col] = 0
        idx +=1



N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

shark_row = shark_col = ((N + 1) // 2) - 1
indexes = update_indexes(shark_row, shark_col)
answer_cnt = [0] * 5

for _ in range(M):
    d, s = map(int, input().split())
    destroy(d, s)
    move()
    while True :
        result = bomb()
        if not result :
            break
        move()
    tmp_answer = update()
    update_A(tmp_answer)


answer = 0
for i in range(1, 4) :
    answer += (i * answer_cnt[i])
print(answer)