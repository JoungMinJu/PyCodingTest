import copy

dR = [-1, -1, 0, 1, 1, 1, 0, -1]
dC = [0, -1, -1, -1, 0, 1, 1, 1]

m_dR = [-1, 0, 1, 0]
m_dC = [0, -1, 0, 1]


def valid_range(row, col):
    return 0 <= row < 4 and 0 <= col < 4


def monster_move():
    new_monster = [[list() for _ in range(4)] for _ in range(4)]
    for row in range(4):
        for col in range(4):
            if len(monster[row][col]) >= 1:
                flag = 0
                for idx in monster[row][col] :
                    for i in range(8) :
                        next_row, next_col = row + dR[(idx+i)%8], col + dC[(idx+i)%8]
                        if not valid_range(next_row, next_col):
                            continue
                        if dead_monster[next_row][next_col] <= 0 and [next_row, next_col] != [pack_row, pack_col]:
                            new_monster[next_row][next_col].append((idx+i)%8)
                            break
    return new_monster


def pack_man_move(monster_pos):
    global pack_row, pack_col
    for row, col in monster_pos:
        if len(monster[row][col]) >= 1 :
            monster[row][col] = list()
            dead_monster[row][col] = 3
    pack_row, pack_col = monster_pos[-1]


def dfs(row, col, cnt, monster_cnt, pos):
    global max_monster_cnt
    global monster_pos
    if cnt >= 3:
        if monster_cnt <= max_monster_cnt:
            return
        max_monster_cnt = monster_cnt
        monster_pos = copy.copy(pos)
        return
    for idx in range(4):
        next_row, next_col = row + m_dR[idx], col + m_dC[idx]
        if not valid_range(next_row, next_col):
            continue
        if [next_row, next_col] not in pos :
            pos.append([next_row, next_col])
            dfs(next_row, next_col, cnt + 1, monster_cnt + len(monster[next_row][next_col]), pos)
            pos.pop()


def update_dead_monster():
    for row in range(4):
        for col in range(4):
            if dead_monster[row][col]:
                dead_monster[row][col] -= 1

def get_tmp_egg() :
    tmp_egg = []
    for row in range(4) :
        for col in range(4) :
            if len(monster[row][col]) >= 1 :
                for d in monster[row][col] :
                    tmp_egg.append([row, col, d])
    return tmp_egg

def duplicate_monster(egg) :
    for r, c, d in egg :
        monster[r][c].append(d)

M, T = map(int, input().split())
pack_row, pack_col = map(int, input().split())
pack_row, pack_col = pack_row - 1, pack_col - 1
# 몬스터 정보 받음
egg = []
for _ in range(M):
    r, c, d = map(int, input().split())
    egg.append([r - 1, c - 1, d - 1])

monster = [[list() for _ in range(4)] for _ in range(4)]
dead_monster = [[0 for _ in range(4)] for _ in range(4)]
max_monster_cnt = -1
for r, c, d in egg:
    monster[r][c].append(d)

for _ in range(T):
    # 몬스터 이동
    monster = monster_move()
    # 팩맨 이동
    #  이동 좌표 받아옴
    max_monster_cnt = -1
    monster_pos = []
    dfs(pack_row, pack_col, 0, 0, [])
    pack_man_move(monster_pos)
    # 몬스터 시체 소멸
    update_dead_monster()
    # 현재 몬스터 가져오기
    tmp_egg = get_tmp_egg()
    duplicate_monster(egg)
    egg += tmp_egg

# 총 몬스터 개수
print(len(egg))
