# 누적합으로 효율성 높이기!!

def solution(board, skill):
    answer = 0
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        tmp[r1][c1] += degree if type == 2 else -degree
        tmp[r1][c2 + 1] += -degree if type == 2 else degree
        tmp[r2 + 1][c1] += -degree if type == 2 else degree
        tmp[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    # 행 기준 누적합
    for i in range(len(tmp) - 1):
        for j in range(len(tmp[0]) - 1):
            tmp[i][j + 1] += tmp[i][j]
    # 열기준 누적합
    for j in range(len(tmp[0]) - 1):
        for i in range(len(tmp) - 1):
           tmp[i+1][j] += tmp[i][j]
    # 기존 배열과 합침
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            board[i][j] += tmp[i][j]
            if board[i][j] > 0 :
                answer += 1
    return answer