# priorities = 이동 우선순위
# smell
# data = 현재 상어 위치
def update_smell() :
    for row in range(N) :
        for col in range(N) :
            if smell[row][col] > 0 :  # 냄새가 남아 있으면
                smell[row][col] -= 1
            if data[row][col] : # 상어가 있으면
                smell[row][col] = [data[row][col], K] # 번호, 시간

def move() :
    new_data = [[0] * N for _ in range(N)]
    for row in range(N) :
        for col in range(N) :
            if data[row][col] : # 상어가 있으면
                direction = directions[data[row][col]-1] # 현재 방향 가져옴
                found = 0
                for idx in priorities[data[row][col]-1][direction-1] : # 우선순위 따라서 네 방향 탐색
                    next_row, next_col = row + dR[idx-1], col + dC[idx-1]
                    if 0 <= next_row < N and 0 <= next_col < N :
                        if not smell[next_row][next_col] : # 냄새 안나면
                            directions[data[row][col]-1] = idx # 그 방향으로 회전하고
                            if not new_data[next_row][next_col] : # 그 칸에 상어가 없으면
                                new_data[next_row][next_col] = data[row][col] # 현재 상어 번호 집어넣기
                            else : # 상어가 있으면
                                new_data[next_row][next_col] = min(new_data[next_row, next_col], data[row][col])
                            found = 1 # 여튼 이동 시켰으니까
                            break # 다음 방향은 확인 안함.
                if not found : # 못찾았음
                    for idx in priorities[data[row][col]-1][direction-1] :
                        next_row, next_col = row + dR[idx-1], col + dC[idx-1]
                        if 0 <= next_row < N and 0 <= next_col < N :
                            if smell[next_row][next_col][0] == data[row][col] : # 자신의 냄새
                                directions[data[row][col] -1 ] = idx
                                new_data[next_row][next_col] = data[row][col]
                                break
    return new_data


N, M, K = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]
shark = [[0,0] for _ in range(M)]

directions = list(map(int, input().split()))

priorities = []
for shark in range(M) :
    tmp = []
    for d in range(4) :
        tmp.append(list(map(int, input().split())))
    priorities.append(tmp)

dR = [-1, 1, 0, 0]
dC = [0, 0, -1, 1]

smell = [[[0,0]] * N for _ in range(N)] # 보드 초기화
answer = 0
while True :
    update_smell()
    data = move()
    answer += 1
    check = 1
    for row in range(N) :
        for col in range(N) :
            if data[row][col] > 1 :
                check = 0
    if check :
        print(answer)
        break
    if answer >= 1000 :
        print(-1)
        break
