import sys

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

def solution(x, y, N) :
    color = paper[x][y]
    for row in range(x, x+N) :
        for col in range(y, y+N) :
            if paper[row][col] != color :
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
    if color == 0 :
        result.append(0)
    else :
        result.append(1)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

result = []
