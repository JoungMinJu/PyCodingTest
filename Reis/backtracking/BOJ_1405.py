# 절대/상대 오차는 10-9 까지 허용한다.
# == 최소 소수점 9자리까지는 출력을 하라는 소리
import sys
input = sys.stdin.readline

def dfs(row, col, count, properties) :
    global final_answer
    if count == n :
        final_answer += properties
        return
    for index in range(4) :
        next_row = row + dR[index]
        next_col = col + dC[index]
        if next_row not in range(length) or next_col not in range(length) or values[index] == 0:
            continue
        if not visited[next_row][next_col] :
            visited[next_row][next_col] = True
            properties *= (values[index] / 100)
            dfs(next_row, next_col, count+1, properties)
            properties /= (values[index]/100)
            visited[next_row][next_col] = False


n, E, W, S, N = map(int, input().split())
length = 2 * n + 1
visited = [[False for _ in range(length)] for _ in range(length)]
dR = [0, 0, -1, 1]
dC = [1, -1, 0, 0]
values = [E, W, S, N]

final_answer = 0.0

start_row, start_col = n, n
visited[start_row][start_col] = True
dfs(start_row, start_col, 0, 1.0)

print(final_answer)
