import sys

input = lambda: sys.stdin.readline().rstrip()


def sum_cal(x1, y1, x2, y2):
    return S[x2][y2] - S[x2][y1 - 1] - S[x1 - 1][y2] + S[x1 - 1][y1 - 1]


N, M = map(int, input().split())

rectangle_input = [[0 for _ in range(M + 1)]]
for _ in range(N):
    line_input = [0] + list(map(int, list(input())))
    rectangle_input.append(line_input)

ans = 0

# 합을 저장할 리스트
S = [[0] * (M + 1) for _ in range(N + 1)]

# 리스트 S는 입력받은 직사각형의 1, 1부터 영역 내의 모든 수의 합을 저장
for row in range(1, N + 1):
    for col in range(1, M + 1):
        S[row][col] = S[row - 1][col] + S[row][col - 1] - S[row - 1][col - 1] + rectangle_input[row][col]

# 첫 번쨰 => 전체 직사각형을 세로로만 분할
for i in range(1, M - 1):
    for j in range(i + 1, M):
        r1 = sum_cal(1, 1, N, i)
        r2 = sum_cal(1, i + 1, N, j)
        r3 = sum_cal(1, j + 1, N, M)
        ans = min(ans, r1 * r2 * r3)

# 두 번째 경우 => 전체 직사각형을 가로로만 분할
for i in range(1, N - 1):
    for j in range(i + 1, N):
        r1 = sum_cal(1, 1, i, M)
        r2 = sum_cal(i + 1, 1, j, M)
        r3 = sum_cal(j + 1, 1, N, M)
        ans = min(ans, r1 * r2 * r3)

# 세 번째 경우 => 전체 세로 분할 후 우측 가로 분할
for i in range(1, M) :
    for j in range(1, N) :
        r1 = sum_cal(1, 1, N, i)
        r2 = sum_cal(1, i+1, j, M)
        r3 = sum_cal(j+1, i+1, N, M)
        ans = min(ans, r1 * r2 * r3)

# 네 번째 경우 => 전체 세로 분할 후 좌측 가로 분할
for i in range(1, N) :
    for j in range(1, M) :
        r1 = sum_cal(1, 1, i, j)
        r2 = sum_cal(i+1, 1, N, j)
        r3 = sum_cal(1, j+1, N, M)
        ans = min(ans, r1 * r2 * r3)

# 다섯 번째 경우 => 전체 가로 분할 후 하단 세로 분할
for i in range(1, N) :
    for j in range(1, M) :
        r1 = sum_cal(1, 1, i, M)
        r2 = sum_cal(i+1, 1, N, j)
        r3 = sum_cal(i+1, j+1, N, M )
        ans = min(ans, r1 * r2 * r3)

# 여섯 번째 경우 => 전체 가로 분할 후 상단 세로 분할
for i in range(1, N) :
    for j in range(1, M) :
        r1 = sum_cal(1, 1, i, j)
        r2= sum_cal(1, j+1, i, M)
        r3 = sum_cal(i+1, 1, N, M)
        ans = min(ans, r1 * r2 * r3)

print(ans)
