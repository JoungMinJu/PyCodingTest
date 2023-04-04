import copy

def move() :
    new_fish = [[list() for _ in range(4)] for _ in range(4)]
    for row in range(4) :
        for col in range(4) :
            if len(fish[row][col]) != 0 :
                for fish_d in fish[row][col] :
                    next_fish_d = fish_d
                    success = 0
                    while True :
                        next_row, next_col = row + dR[next_fish_d], col + dC[next_fish_d]
                        if not valid_range(next_row, next_col) or smell[next_row][next_col] or [next_row, next_col] == [shark_row, shark_col] :
                            next_fish_d = get_fish_direction(next_fish_d)
                            if next_fish_d == fish_d :
                                break
                        else : # 이동 가능하면
                            new_fish[next_row][next_col].append(next_fish_d)
                            success = 1
                            break
                    if not success : # 실패했으면
                        new_fish[row][col].append(fish_d) # 기존 위치 넣어주기
    return new_fish

def get_fish_direction(d) :
    if d == 0 :
        return 7
    return d - 1

def dfs(row, col, direction, fish_cnt, visited) :
    if direction >= 100 :
        candidates.append([fish_cnt, direction])
        return
    for idx in range(1,5) :
        next_row, next_col = row + dR2[idx], col + dC2[idx]
        if not valid_range(next_row, next_col) :
            continue
        if len(new_fish[next_row][next_col]) > 0 and not  [next_row, next_col] in visited: # 물고기가 있는데 셀 수 있으면
            visited.append([next_row, next_col])
            dfs(next_row, next_col, direction * 10 + idx, fish_cnt + len(new_fish[next_row][next_col]), visited)
            visited.pop()
        else :
            dfs(next_row, next_col, direction * 10 + idx, fish_cnt, visited)

def shark_move(direciton_info) :
    global shark_row, shark_col
    cnt, info = direciton_info
    info = list(str(info))
    for i in info :
        i = int(i)
        shark_row += dR2[i]
        shark_col += dC2[i]
        if len(new_fish[shark_row][shark_col]) > 0 :
            new_fish[shark_row][shark_col].clear()
            smell[shark_row][shark_col] = 3

def update_smell() :
    for row in range(4) :
        for col in range(4) :
            if smell[row][col] > 0 :
                smell[row][col] -= 1

def duplicate() :
    for row in range(4) :
        for col in range(4) :
            if len(fish[row][col]) > 0 :
                new_fish[row][col].extend(fish[row][col])

def valid_range(row, col) :
    return 0 <= row < 4 and 0 <= col < 4

dR = [0, -1, -1, -1, 0, 1, 1, 1]
dC = [-1, -1, 0, 1, 1, 1, 0, -1]

dR2 = [0, -1, 0, 1, 0]
dC2 = [0, 0, -1, 0, 1]

M, S = map(int, input().split())  # 물고기의 수, 마법을 연습한 횟수
fish = [[list() for _ in range(4)] for _ in range(4)]
for _ in range(M) :
    row, col, direction = map(int, input().split())
    fish[row-1][col-1].append(direction-1)
    fish.append([row-1, col-1, direction -1])

shark_row, shark_col = map(int, input().split())
shark_row -= 1
shark_col -= 1

smell = [[0] * 4 for _ in range(4)] #  smell 남기기
for magic in range(S) :
    # 이동
    new_fish = move()
    # 상어 이동
    candidates = [] # 물고기 개수, direction
    dfs(shark_row, shark_col, 0, 0, [])
    candidates.sort(key = lambda x : (-x[0], x[1]))
    # 해당 direciton에 맞게 이동시키기 (이동시키는 과정에서 물고기 삭제 + 냄새 남기기)
    shark_move(candidates[0])
    # 물고기 냄새 제거
    update_smell()
    # 복제
    duplicate()
    # 바꾸기
    fish = copy.deepcopy(new_fish)

answer = 0
for row in range(4) :
    for col in range(4) :
        if len(fish[row][col]) > 0 :
            answer += len(fish[row][col])
print(answer)