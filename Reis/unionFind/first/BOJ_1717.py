import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def find(now_node):
    if now_node == parent[now_node]:
        return now_node
    p = find(parent[now_node])
    parent[now_node] = p
    return parent[now_node]


def union(node_a, node_b):
    parent_a = find(node_a)
    parent_b = find(node_b)
    if parent_a == parent_b:
        return
    if parent_a < parent_b:  # 작은 수가 부모가 되도록
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


N, M = map(int, input().split())

# 부모 테이블 생성
parent = []
for node in range(N + 1):
    parent.append(node)

for _ in range(M):
    command, node1, node2 = map(int, input().split())
    if command == 0:
        union(node1, node2)
    elif command == 1:
        if find(node1) == find(node2):
            print("YES")
        else:
            print("NO")
