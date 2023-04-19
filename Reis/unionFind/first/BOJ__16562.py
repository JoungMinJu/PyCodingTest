from sys import stdin

parents = []
charges = []

def find(x: int) -> int:
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    # 친구비를 기준으로 부모 설정
    if charges[x] < charges[y]:
        parents[y] = x
    else:
        parents[x] = y

def main():
    def input():
        return stdin.readline().rstrip()
    global parents, charges

    n, m, k = map(int, input().split())
    parents = list(i for i in range(n + 1))
    charges = [0] + list(map(int, input().split()))
    for _ in range(m):
        v, w = map(int, input().split())
        union(v, w)

    friends = set()
    cost = 0
    # 친구들 중 parent인 친구의 요금 총합 구하기
    for i in range(1, n + 1):
        if find(i) not in friends:
            cost += charges[parents[i]]
            friends.add(parents[i])

    if cost > k:
        print("Oh no")
    else:
        print(cost)


if __name__ == "__main__":
    main()