

N, M, T = map(int, input().split()) # 1~N의 원판 // M개의 정수가 적혀있고
# 없는 번호 0으로 바꾸기
numbers =  [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(T)]


def get_sum_and_count() :
    tmp = 0
    count = 0
    for row in range(N) :
        for col in range(M) :
            tmp += numbers[row][col]
            if numbers[row][col] != 0 :
                count += 1
    return tmp, count


for i in range(T) :
    x, d, k = moves[i]

    for _ in range(k) :
        for idx in range(x, N+1, x) :
            idx -=1
            if d == 1 :
                numbers[idx] = numbers[idx][1:] + [numbers[idx][0]]
            else :
                size = len(numbers[idx])
                numbers[idx] = [numbers[idx][size-1]] + numbers[idx][:size-1]

    # 행 방향 검증
    removed_indexes = set()
    for row in range(N) :
        for col in range(M) :
            now = numbers[row][col]
            before = numbers[row][col-1]
            if now != 0 and before != 0 :
                if now == before :
                    removed_indexes.add((row, col-1))
                    removed_indexes.add((row, col))
    for col in range(M) :
        for row in range(N-1) :
            now = numbers[row][col]
            after = numbers[row+1][col]
            if now != 0 and after != 0 :
                if now == after :
                    removed_indexes.add((row, col))
                    removed_indexes.add((row+1, col))
    # 0으로 바꿔치기
    if len(removed_indexes) == 0 :
        total_sum, total_count = get_sum_and_count()
        if total_count == 0 :
            total_mean = 0
        else :
            total_mean = total_sum / total_count
        for row in range(N) :
            for col in range(M) :
                now = numbers[row][col]
                if now != 0 :
                    if total_mean - now > 0:
                        numbers[row][col] += 1
                    elif total_mean - now < 0:
                        numbers[row][col] -= 1
    else :
        for index in removed_indexes:
            numbers[index[0]][index[1]] = 0

answer = get_sum_and_count()
print(answer[0])
