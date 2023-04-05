import copy
from collections import deque

is_valid = lambda row, col : 0 <= row < N and 0 <= col < N

def solve():
    count = 0
    while que:
        size = len(que)
        count += 1
        # max 5번 처리해주기
        if count > 5 :
            return
        for _ in range(size):
            now_graph = que.popleft()
            for idx in range(4):
                next_graph = move(now_graph, idx)
                str_next_graph = to_string(next_graph)
                if str_next_graph not in check:
                    check.append(str_next_graph)
                    que.append(next_graph)


def to_string(g):
    tmp = ""
    for row in range(N):
        for col in range(N):
            tmp += str(g[row][col])
    return tmp


def move(g, idx):
    if idx in (0, 1) :
        return move_width(g, idx)
    return move_height(g, idx)



def move_width(before_g, idx) :
    global answer
    g = copy.deepcopy(before_g)
    check = [[0] * N for _ in range(N)]
    start, end, gap = moving[idx]
    for col in range(start, end, gap):
        for row in range(0, N) :
            now_num = g[row][col]
            next_row, next_col = row + dR[idx], col + dC[idx]
            if is_valid(next_row, next_col):
                if g[next_row][next_col] == now_num and not check[next_row][next_col] :
                    check[next_row][next_col] = 1
                    g[next_row][next_col] += g[row][col]
                    g[row][col] = 0
                    answer = max(answer, g[next_row][next_col])
                elif g[next_row][next_col] == 0:
                    g[next_row][next_col] = g[row][col]
                    g[row][col] = 0
    return g

def move_height(before_g, idx) :
    global answer
    g = copy.deepcopy(before_g)
    check = [[0] * N for _ in range(N)]
    start, end, gap = moving[idx]
    for row in range(0, N):
        for col in range(start, end, gap) :
            now_num = g[row][col]
            next_row, next_col = row + dR[idx], col + dC[idx]
            if is_valid(next_row, next_col):
                if g[next_row][next_col] == now_num and not check[next_row][next_col] :
                    check[next_row][next_col] = 1
                    g[next_row][next_col] += g[row][col]
                    g[row][col] = 0
                    answer = max(answer, g[next_row][next_col])
                elif g[next_row][next_col] == 0:
                    g[next_row][next_col] = g[row][col]
                    g[row][col] = 0
    return g

N = int(input())
answer = -float('inf')
graph = []

# 우 좌 상 하
dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]
moving = [[N - 1, -1, -1], [0, N, 1], [0, N, 1], [N - 1, -1, -1]]

for _ in range(N):
    tmp = list(map(int, input().split()))
    answer = max(answer, max(tmp))
    graph.append(tmp)

que = deque()
que.append(graph)
count = -1
check = []

solve()
print(answer)