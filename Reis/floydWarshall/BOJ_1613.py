import sys

input = lambda : sys.stdin.readline().rstrip()

def floyd_warshall() :
    for middle in range(N) :
        for start in range(N) :
            for end in range(N) :
                if matrix[start][middle] and matrix[middle][end] :
                    matrix[start][end] = 1

N, K = map(int, input().split())
matrix = [[0] * N for _ in range(N)]

for _ in range(K) :
    A, B = map(int, input().split())
    matrix[A-1][B-1] = 1

floyd_warshall()

S = int(input())

for _ in range(S) :
    A, B = map(int, input().split())
    if matrix[A-1][B-1] :
        print(-1)
    elif matrix[B-1][A-1] :
        print(1)
    else :
        print(0)
