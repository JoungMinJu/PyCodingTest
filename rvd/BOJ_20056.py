dR = [-1, -1, 0, 1, 1, 1, 0, -1]
dC = [0, 1, 1, 1, 0, -1, -1, -1]

valid_range = lambda row, col : 0 <= row < N and 0 <= col < N

# 파이어볼 M개 발사
# 위치 r,c 질량 m, 방향 d, 속력 s

N, M, K = map(int, input().split())
fireballs = []
for _ in range(M) :
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s,d])

map = [[[] for _  in range(N)] for _ in range(N)]

for _ in range(K) :
    while fireballs : # 파이어볼 모두!
        now_row, now_col, now_m, now_s, now_d = fireballs.pop()
        next_row = (now_row + now_s + dR[now_d]) % N
        next_col = (now_col + now_s + dC[now_d]) % N
        map[next_row][next_col].append([now_m, now_s, now_d]) # 그 위치에 넣기

    for row in range(N) :
        for col in range(N) :
            if len(map[row][col]) > 1 : # 두 개 이상의 파이어볼
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(map[row][col])
                while map[row][col] :  # 각 파이어볼 체크
                    m, s, d = map[row][col].pop()
                    sum_m += m
                    sum_s += s
                    if d % 2 :
                        cnt_odd += 1
                    else :
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt :
                    next_direction = [0,2, 4,6]
                else :
                    next_direction = [1, 3, 5,7]
                if sum_m / 5 : # 질량 0이면 소멸
                    for d in next_direction :
                        fireballs.append([row, col, sum_m/5, sum_s/cnt, d])
            if len(map[row][col]) == 1 : # 한개면
                 fireballs.append([row, col] + map[row][col].pop()) # 비워줘야 하니까

print(sum([f[2] for f in fireballs]))