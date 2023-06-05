import sys

sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().rstrip()

def func(row, col, cnt) :
    global ans
    if col >= 10 :
        ans = min(ans, cnt)
        return
    if row >= 10 :
        func(0, col+1, cnt)
        return
    if a[row][col] :
        for k in range(5) :
            if paper[k] == 5 :
                continue
            if row + k >= 10 or col + k >= 10 :
                continue
            flag = 0
            for i in range(row, row + k + 1) :
                for j in range(col, col + k + 1) :
                    if a[i][j] == 0 :
                        flag = 1
                        break
                if flag :
                    break
            if not flag :
                for i in range(row, row + k + 1) :
                    for j in range(col, col + k +1) :
                        a[i][j] = 0
                paper[k] += 1
                func(row + k + 1, col, cnt +1)
                paper[k] -= 1
                for i in range(row, row+k+1) :
                    for j in range(col, col + k + 1) :
                        a[i][j] = 1
    else :
        func(row+1, col, cnt)

func(0, 0, 0)
print(ans) if ans != float('inf') else print(-1)



a = [list(map(int, input().split())) for _ in range(10)]
paper = [0] * 5
ans = float('inf')

