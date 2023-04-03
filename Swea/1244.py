def recur(cnt, n) :
    global answer
    if cnt == n :
        tmp = "".join(board)
        if answer < tmp :
            answer = tmp
        return
    for i in range(len_board) :
        for j in range(i+1, len_board) :
            board[i], board[j] = board[j], board[i]
            tmp = ''.join(board)
            if visited.get((tmp, cnt), 1) :
                visited[(tmp, cnt)] = 0
                recur(cnt+1, n)
            board[i], board[j] = board[j], board[i]



test_size = int(input())
for test in range(1, test_size+1) :
    board, n = input().split()
    n = int(n)
    board = list(board)
    len_board = len(board)
    visited = {}
    answer = "00000000"
    recur(0, n)
    print("#{} {}".format(test, answer))