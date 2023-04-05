from copy import deepcopy
from collections import deque

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

N, M, D = map(int, input().split())

def valid_range(row, col) :
    return 0 <= row < N and 0 <= col < M

# 궁수 = col
def dfs(idx, archers) :
    if len(archers) == 3:
        # 배열 복사
        now_board = deepcopy(board)
        solve(now_board, archers, monster_cnt)
        return
    if idx >= M :
        return
    archers.append(idx)
    dfs(idx+1, archers)
    archers.pop()
    dfs(idx+1, archers)

def solve(now_board, archers, monster_cnt) :
    global answer
    now_answer = 0
    while monster_cnt > 0 :
        monsters = set()
        for archer in archers :
            m_row, m_col = find_monster(now_board, archer)
            if [m_row,m_col] != [-1, -1] :
                monsters.add(find_monster(now_board, archer))
        # 지우기
        for row, col in monsters :
            now_board[row][col] = 0
        monster_cnt -= len(monsters)
        now_answer += len(monsters)
        # 움직이기
        monster_cnt -= sum(now_board[N-1])
        now_board = [[0] * M] + now_board[:N-1]
    answer = max(now_answer, answer)


def find_monster(now_board, archer) :
    que = deque()
    visited = [[N, archer]]
    que.append([N, archer])
    cnt = 0
    while que :
        size = len(que)
        cnt +=1
        if cnt > D:
            return -1, -1
        candidates = []
        for _ in range(size) :
            now_row, now_col = que.popleft()
            for idx in range(4) :
                next_row, next_col = now_row + dR[idx], now_col + dC[idx]
                if not valid_range(next_row, next_col) :
                    continue
                if not [next_row, next_col] in visited :
                    if now_board[next_row][next_col] :
                        candidates.append([next_row, next_col])
                    else :
                        que.append([next_row, next_col])
                        visited.append([next_row, next_col])
        if len(candidates) > 0 :
            candidates.sort(key=lambda x : x[1])
            return candidates[0][0], candidates[0][1] # 첫 번째 제출

def move_monster(now_board) :
    return [0] * M + now_board[:N]

monster_cnt = 0
board = []
for row in range(N) :
    tmp = list(map(int, input().split()))
    monster_cnt += sum(tmp)
    board.append(tmp)

answer = -1
dfs(0, [])
print(answer)
