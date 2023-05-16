import sys

input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(10)]
papers = [0] * 5
answer = sys.maxsize

def func(row, col, cnt) :
    global ans
    if col >= 10 :
        ans = min(ans, cnt)
        return
    if row >= 10 :
        func(0, col+1, cnt)
        return
    if graph[row][col] == 1:
        for k in range(5) :
            if papers[k] == 5:
                continue
            if row + k >= 10 or col + k >= 10 :
                continue
            flag = 0
            for i in range(row, row+k+1) :
                for j in range(col, col+k+1) :
                    if graph[i][j] == 0 :
                        flag = 1
                        break
                if flag :
                    break
            if not flag :
                for i in range(row, row + k + 1) :
                    for j in range(col, col + k + 1) :
                        graph[row][col] = 0 # 색종이 붙여줌
                papers[k] += 1
                func(row + k + 1, col, cnt+1)
                papers[k] -= 1
                for i in range(row, row + k + 1) :
                    for j in range(col, col + k + 1) :
                        graph[row][col] = 1 # 색종이 뗌
    else :
        func(row + 1, col, cnt)

func(0, 0, 0)
if answer != sys.maxsize :
    print(answer)
else :
    print(-1)