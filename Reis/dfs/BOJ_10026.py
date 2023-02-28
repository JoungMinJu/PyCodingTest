import sys
input = sys.stdin.readline

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

def dfs(row, col, type,  color) :
    if type == 'weakness' and color in ('G', 'R') :
        now_color = ('G', 'R')
    else :
        now_color = list(color)
    if type == 'normal' :
        now_visited = visited_normal
    else :
        now_visited = visited_weakness

    now_visited[row][col] = True
    for idx in range(4):
        next_row = row + dR[idx]
        next_col = col + dC[idx]
        if next_col < 0 or next_col >= N or next_row < 0 or next_row >= N :
            continue
        if not now_visited[next_row][next_col] and map[next_row][next_col] in now_color:
            dfs(next_row, next_col, type, now_color)


N = int(input())
map = [list(input().strip()) for _ in range(N)]
visited_normal = [[False]*N for _ in range(N)]
visited_weakness = [[False]*N for _ in range(N)]

normal_count, weakness_count = 0, 0

for row in range(N):
    for col in range(N):
        if not visited_normal[row][col]:
            dfs(row, col, "normal", map[row][col])
            normal_count+=1
        if not visited_weakness[row][col]:
            dfs(row, col, 'weakness', map[row][col])
            weakness_count += 1

print(normal_count, weakness_count)