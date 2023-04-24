N = int(input()) # 지방의 수
money = list(map(int, input().split()))
money.sort()
M = int(input())

def get_need_money(max_money):
    answer = 0
    for m in money :
        if m >= max_money :
            answer += max_money
        else :
            answer += m
    return answer

min_money = 0
max_money = money[-1]
while min_money <= max_money :
    mean_money = (min_money + max_money) // 2
    need_money = get_need_money(mean_money)
    if need_money <= M :
        min_money = mean_money+1
    else :
        max_money = mean_money -1


print(max_money)