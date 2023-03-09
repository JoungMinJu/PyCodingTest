import sys
from collections import deque

input = sys.stdin.readline

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

TARGET = "123456789"

def bfs() :
    while que :
        now = que.popleft()
        if now == TARGET :
            return cntDict[now]
        empty_space = now.find("9")
        empty_row = empty_space // 3
        empty_col = empty_space % 3

        for idx in range(4) :
            next_row = empty_row + dR[idx]
            next_col = empty_col + dC[idx]

            if 0 <= next_row < 3 and 0 <= next_col < 3 :
                next_empty_space = next_row * 3 + next_col
                next_num  = list(now)
                next_num[next_empty_space], next_num[empty_space] = next_num[empty_space], next_num[next_empty_space]
                next_num = "".join(next_num)

                if not cntDict.get(next_num) :
                    que.append(next_num)
                    cntDict[next_num] = cntDict[now] + 1
    return -1


start = ""
for _ in range(3) :
    tmp = input().strip().replace(" ", "")
    start += tmp

start = start.replace("0", "9")

que = deque()
que.append(start)
cntDict = dict()
cntDict[start] = 0

print(bfs())