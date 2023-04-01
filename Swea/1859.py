test_size = int(input())
for test in range(test_size) :
    N = int(input())
    price = list(map(int, input().split()))
    after = price[-1]
    _cnt = _sum = 0
    answer = 0
    for idx in range(len(price)-2, -1, -1) :
        if price[idx] <= after :
            _cnt += 1
            _sum += price[idx]
        else :
            answer += (after*_cnt) - _sum
            _cnt = _sum = 0
            after = price[idx]
    answer += (after*_cnt) - _sum
    print(f"#{test} {answer}")