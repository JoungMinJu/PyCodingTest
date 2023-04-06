
def valid_range(row, col):
    return 0 <= row < N and 0 <= col < N

def spread_smell(shark) :
    for idx in range(1, M+1) :
        s_row, s_col = shark[idx]
        if [s_row, s_col] == [-1, -1] :
            continue
        smell[s_row][s_col] = [idx, K]

def update_smell():
    for row in range(N) :
        for col in range(N) :
            if smell[row][col][1] :
                smell[row][col][1] -= 1

def update_shark(shark) :
    new_shark = [[-1,-1]]
    for idx in range(1, M+1) :
        now_shark = shark[idx]
        if not now_shark in new_shark :
            new_shark.append(now_shark)
        else :
            new_shark.append([-1,-1])
    return new_shark

def get_shark_cnt(shark) :
    return M + 1 - shark.count([-1,-1])


dR = [0, -1, 1, 0, 0]
dC = [0, 0, 0, -1, 1]

N, M, K = map(int, input().split())

smell = [[[-1, 0]] * N for _ in range(N)]
shark = [[-1, -1] for _ in range(M+1)]
shark_direction = [-1] * (M+1)
for row in range(N):
    tmp = list(map(int, input().split()))
    for col in range(N):
        if tmp[col]:
            shark[tmp[col]] = [row, col]

tmp = list(map(int, input().split()))
for s in range(1, M + 1):
    shark_direction[s] = tmp[s - 1]

d_info = {}
for s in range(1, M+1) :
    tmp = [list(map(int, input().split())) for _ in range(4)]
    d_info[s] = tmp

# 초기 냄새 뿌리기
time = 0
shark_cnt = M
while time < 1000:
    spread_smell(shark)
    time += 1
    for sh in range(1, M+1) :
        s_row, s_col = shark[sh]
        if [s_row, s_col] == [-1, -1] :
            continue
        now_d = shark_direction[sh]
        candidates = []
        flag = 0
        for idx in range(4) :
            next_move_idx = d_info[sh][now_d-1][idx]
            next_s_row, next_s_col = s_row + dR[next_move_idx], s_col + dC[next_move_idx]
            if not valid_range(next_s_row, next_s_col) :
                continue
            if smell[next_s_row][next_s_col][1] == 0 :
                flag = 1
                break
            elif smell[next_s_row][next_s_col][0] != sh :
                continue
            elif smell[next_s_row][next_s_col][0] == sh :
                candidates.append([next_s_row, next_s_col, next_move_idx])
        if not flag and len(candidates) > 0 :
            next_s_row, next_s_col, next_move_idx = candidates[0]
        shark[sh] = [next_s_row, next_s_col]
        shark_direction[sh] = next_move_idx
    shark = update_shark(shark)
    shark_cnt = get_shark_cnt(shark)
    if shark_cnt == 1 :
        break
    update_smell()

    # for 샤크
    # 우선순위 찾아서 이동
    # 냄새 뿌리기
    # 냄새 하나 빼기
if time >= 1000 and shark_cnt > 1 :
    print(-1)
else :
    print(time)