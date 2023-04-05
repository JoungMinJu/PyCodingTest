valid_range = lambda row, col : 0 <= row < 101 and 0 <= col < 101

N = int(input())

graph = [[0] * 101 for _ in range(101)] # 101 x  101 행렬
dR = [0, -1, 0, 1]
dC = [1, 0, -1, 0]

for _ in range(N) :
    col, row, direction, generation = map(int, input().split()) # 시작 x, 시작 y, 방향, 세대
    graph[row][col] = 1 # 시작 점 체크

    curves = [direction] # 커브 리스트 만든다.
    for gen in range(generation) :
        for curve_idx in range(len(curves) - 1, -1, -1) :
            curves.append((curves[curve_idx] + 1) % 4)
    for curve in curves :
        row += dR[curve]
        col += dC[curve]
        if not valid_range(row, col) :
            continue
        graph[row][col] = 1

answer = 0
for row in range(101):
    for col in range(101) :
        # 사각형 체크
        if not valid_range(row+1, col +1 ):
            continue
        if graph[row][col] == 1 and graph[row + 1][col] == 1 and graph[row][col + 1] == 1 and graph[row + 1][col + 1] == 1:
            answer += 1
print(answer)