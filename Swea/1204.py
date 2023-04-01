test_size = int(input())
for test in range(test_size) :
    test_num = int(input())
    score = list(map(int, input().split()))
    max_cnt = -1
    answer = -1
    for s in range(101) :
        _cnt = score.count(s)
        if _cnt >= max_cnt :
            max_cnt = _cnt
            answer = s
    print(f"#{test_num} {answer}")