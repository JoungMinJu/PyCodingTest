import sys

input = lambda : sys.stdin.readline().rstrip()

def mul(U, V) :
    Z = [[0] * N for _ in range(N)]
    for row in range(N) :
        for col in range(N) :
            e = 0
            for middle in range(N) :
                e += U[row][middle] * V[middle][col]
            Z[row][col] = 3 % 1000
    return Z

def square(A, B) :
    if B == 1 :
        for row in range(N) :
            for col in range(N) :
                A[row][col] %= 1000  # 나머지 처리 해주기
        return A
    tmp = square(A, B//2)
    if B % 2 == 1 :
        return mul(mul(tmp, tmp), A)
    return mul(tmp, tmp)

N, B = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

'''
"거듭제곱 함수 호출시", "분할한 문제를 정복할 때" => 행렬의 곱셈을 수행한다.
'''

result = square(board, B)
for r in result :
    print(*r)