def dfs(v, t_sum, k_sum) :
    global max_taste
    if k_sum > L :
        return
    if max_taste < t_sum :
        max_taste = t_sum
    if v == N :
        return
    taste, kcal = ingredients[v]
    dfs(v+1, t_sum+taste, k_sum+kcal)
    dfs(v+1, t_sum, k_sum)

T = int(input())

for test in range(1, T+1) :
    N, L = map(int, input().split())
    ingredients = [list(map(int,input().split())) for _ in range(N)]
    max_taste = 0
    dfs(0,0,0)
    print(f"{test} {max_taste}")