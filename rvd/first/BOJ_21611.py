from collections import deque

N, M = map(int, input().split())
graph = []
cmd = []
score = [0] * 3

def indexing() :
    row = col = N//2
    dR = [0, 1, 0, -1]
    dC = [-1, 0, 1, 0]
    depth = 0

    while True :
        for idx in range(4) :
            if idx % 2 == 0 :
                depth += 1
            for length in range(depth) :
                row += dR[idx]
                col += dC[idx]
                graphIdx.append([row, col])
                if row == 0 and col == 0 :
                    return

def magic(d, s) :
    row = col = N//2
    dR = [-1, 1, 0, 0]
    dC = [0, 0, -1, 1]
    for length in range(s) :
        row += dR[d]
        col += dC[d]
        if row < 0 or row >= N or col < 0 or col >= N :
            break
        graph[row][col] = 0
    fill_blank()
    while bomb() :
        fill_blank()
    grouping()

def fill_blank() :
    blankIdx = deque()
    for row, col in graphIdx:
        if graph[row][col] == 0 :
            blankIdx.append([row, col])
        elif graph[row][col] > 0 and blankIdx :
            next_row, next_col = blankIdx.popleft()
            graph[next_row][next_col] = graph[row][col]
            graph[row][col] = 0
            blankIdx.append([row, col])

def bomb() :
    visited = deque()
    cnt = 0
    num = -1
    flag = 0
    for row, col in graphIdx :
        if num == graph[row][col] :
            visited.append([row, col])
            cnt += 1
        else :
            if cnt >= 4 :
                score[num-1] += cnt
                flag = 1
            while visited :
                next_row, next_col = visited.popleft()
                if cnt >= 4 :
                    graph[next_row][next_col] = 0
            num = graph[row][col]
            cnt = 1
            visited.append([row, col])
    return flag

def grouping() :
    cnt = 1
    tmp_row, tmp_col = graphIdx[0]
    num = graph[tmp_row][tmp_col]
    nums = []

    for i in range(1, len(graphIdx)) :
        row, col = graphIdx[i][0], graphIdx[i][1]
        if num == graph[row][col] :
            cnt += 1
        else :
            nums.append(cnt)
            nums.append(num)
            num = graph[row][col]
            cnt =1
    idx = 0
    for row, col in graphIdx :
        if not nums :
            break
        graph[row][col] = nums[idx]
        idx += 1
        if idx == len(nums) :
            break

graph = [list(map(int, input().split())) for _ in range(N)]
cmd = [list(map(int, input().split())) for _ in range(M)]

graphIdx = deque()
indexing()

for d, s in cmd :
    magic(d-1, s)

answer = 0
for num in range(3) :
    answer += (num + 1) * score[num]
print(answer)