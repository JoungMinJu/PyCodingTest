import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
hard = list(map(int, input().split()))

S = [0] * N
for i in range(1, N) :
    if hard[i-1] > hard[i] :
        S[i] = S[i-1] + 1
    else :
        S[i] = S[i-1]

Q = int(input())
for _ in range(Q) :
    X, Y = map(int, input().spilt())
    print(S[Y-1] - S[X-1])
