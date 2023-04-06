blocks = [  # 각 블록의 +행 +열
    [[0, 0], [0, 1], [0, 2], [0, 3]],  # 1번
    [[0, 0], [1, 0], [2, 0], [3, 0]],  # 2번
    [[0, 0], [0, 1], [1, 0], [1, 1]],  # 3번
    [[1, 0], [1, 1], [1, 2], [0, 2]],  # 4번
    [[0, 0], [1, 0], [1, 1], [1, 2]],  # 5번
    [[0, 0], [0, 1], [0, 2], [1, 0]],  # q번
    [[0, 0], [0, 1], [0, 2], [1, 2]],  # 7
    [[0, 0], [1, 0], [2, 0], [2, 1]],  # 8
    [[0, 1], [1, 1], [2, 1], [2, 0]],  # 9
    [[0, 0], [0, 1], [1, 0], [2, 0]],  # 10
    [[0, 0], [0, 1], [1, 1], [2, 1]],  # 11
    [[0, 0], [1, 0], [1, 1], [2, 1]],  # 12
    [[0, 1], [1, 0], [1, 1], [2, 0]],  # 13
    [[0, 1], [0, 2], [1, 0], [1, 1]],  # 14
    [[0, 0], [0, 1], [1, 1], [1, 2]],  # 15
    [[0, 1], [1, 0], [1, 1], [1, 2]],  # 16
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [1, 0], [1, 1], [2, 0]],
    [[0, 1], [1, 0], [1, 1], [2, 1]]
]

def valid_range(row, col):
    return 0 <= row < N and 0 <= col < M

def get_answer(row, col, block) :
    tmp = 0
    for dR, dC in block :
        tmp += board[row + dR][col + dC]
    return tmp

N, M = map(int, input().split())
board = [[-1000] * (M + 3) for _ in range(N + 3)]
for row in range(N):
    tmp = list(map(int, input().split()))
    for col in range(M):
        board[row][col] = tmp[col]

answer = -1
for row in range(N) :
    for col in range(M) :
        for block in blocks :
            tmp = get_answer(row, col, block)
            answer = max(answer, tmp)
print(answer)