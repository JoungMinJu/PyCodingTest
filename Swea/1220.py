for test in range(1,11) :
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(N)]

    total_res = 0
    for col in range(N) :
        flag = 0
        for row in range(N):
            if mag[row][col] == 1 :
                flag = 1
            elif mag[row][col] == 2 :
                if flag :
                    total_res += 1
                    flag = 0
    print(f"#{test} {total_res}")