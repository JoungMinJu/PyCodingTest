from collections import defaultdict

N, M, K = map(int, input().split())
fireballs = defaultdict(list)
for _ in range(M) :
    r, c, m, s, d = map(int, input().split())
    fireballs[(r-1, c-1)].append((m, s, d))
dR = [-1, -1, 0, 1, 1, 1, 0, -1]
dC = [0, 1, 1, 1, 0, -1, -1, -1]

def move_fireballs() :
    new_fireballs = defaultdict(list)
    for loc, info_list in fireballs.itmes() :
        row, col = loc
        for m, s, d in info_list :
            next_row = (row + dR[d] * s) % N
            next_col = (col + dC[d] * s) % N
            new_fireballs[(next_row, next_col)].append((m,s,d))
    return new_fireballs.copy()

def all_odd_or_even(dirs):
    odd_flag = even_flag = False
    for d in dirs:
        if d % 2 == 1 :
            odd_flag = True
        if d % 2 == 0 :
            odd_flag = True
    if odd_flag and even_flag :
        return False
    return True

def change_duplicate_fireballs() :
    # 난 망했다ㅠ ㅠ ㅠ ㅠ
    new_fireballs = defaultdict(list)
    for loc, info_ilst in fireballs.items():
        if len(info_ilst) == 1:  # 해당 좌표에 파이어볼이 1개인 경우
            new_fireballs[loc].append(info_ilst[0])
            continue

        # 파이어볼이 중복된 경우
        sum_m, sum_s, dirs = 0, 0, []  # 질량합, 속도합, 방향리스트
        for m, s, d in info_ilst:
            sum_m += m
            sum_s += s
            dirs.append(d)
        new_m = int(sum_m / 5)  # 새로운 파이어볼 질량
        if new_m == 0:  # 질량이 0인 경우 소멸되므로 continue
            continue
        new_s = int(sum_s / len(info_ilst))  # 새로운 파이어볼 속도
        new_dirs = [0, 2, 4, 6] if all_odd_or_even(dirs) else [1, 3, 5, 7]  # 새로운 파이어볼 방향(all_odd_or_even() 함수의 결과에 따름)
        for new_d in new_dirs:
            new_fireballs[loc].append((new_m, new_s, new_d))
    return new_fireballs

for _ in range(K) :
    fireballs = move_fireballs()
    fireballs = change_duplicate_fireballs()
result = 0
for loc, info_list in fireballs.items() :
    for m,s,d in info_list :
        result += m
print(result)

