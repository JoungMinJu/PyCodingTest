from copy import deepcopy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

# 위로
def up(board) :
    for col in range(N) :
        pointer = 0 # 포인터로 처음을 집어주고
        for row in range(1, N) : # 뒤에 애들 탐색
            if board[row][col] : # 0이 아니면
                tmp = board[row][col]
                board[row][col] = 0
                # 1. 빈칸
                if board[pointer][col] == 0 :
                    board[pointer][col] = tmp
                # 2. 합칠 수 있을 때
                elif board[pointer][col] == tmp :
                    board[pointer][col] *= 2
                    pointer += 1
                # 3. 못합칠 때
                else :
                    pointer += 1
                    board[pointer][col] = tmp
    return board

# 아래로
def down(board) :
    for col in range(N) :
        pointer = N - 1
        for row in range(N-2, -1, -1) :
            if board[row][col] :
                tmp = board[row][col]
                board[row][col] = 0
                if board[pointer][col] == 0 :
                    board[pointer][col] = tmp
                elif board[pointer][col] == tmp :
                    board[pointer][col] *= 2
                    pointer -= 1
                else :
                    pointer -= 1
                    board[pointer][col] = tmp
    return board

# 왼쪽
def left(board) :
    for row in range(N) :
        pointer = 0
        for col in range(1, N) :
            if board[row][col] :
                tmp = board[row][col]
                board[row][col] = 0
                if board[row][pointer] == 0 :
                    board[row][pointer] = tmp
                elif board[row][pointer] == tmp :
                    board[row][pointer] *= 2
                    pointer += 1
                else :
                    pointer += 1
                    board[row][pointer] = tmp
    return board

# 오른쪽
def right(board) :
    for row in range(N) :
        pointer = N - 1
        for col in range(N-2, -1, -1) :
            if board[row][col] :
                tmp = board[row][col]
                board[row][col] = 0
                if board[row][pointer] == 0:
                    board[row][pointer] = tmp
                elif board[row][pointer] == tmp :
                    board[row][pointer] *= 2
                    pointer -= 1
                else :
                    pointer -= 1
                    board[row][pointer] = tmp
    return board

def dfs(board, cnt) :
    if cnt == 5 :
        return max(map(max, board)) # 2차원 배열 중 가장 큰 값 반환
    # 상하좌우로 움직여 리턴한 값들 중 가장 큰 값 반환
    return max(dfs(up(deepcopy(board)), cnt+1), dfs(down(deepcopy(board)), cnt+1), dfs(left(deepcopy(board)),cnt+1), dfs(right(deepcopy(board)),cnt + 1))
print(dfs(board, 0))
