import sys
from collections import defaultdict, deque

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
connection = defaultdict(list)
start, end = map(int, input().split())
connection_length = int(input())
for _ in range(connection_length)  :
    conn1, conn2 = map(int, input().split())
    connection[conn1].append(conn2)
    connection[conn2].append(conn1)

def bfs(start, end) :
    visited = [-1] * (N+1)  # idx 번째 사람 이미 방문했는지
    que = deque()
    visited[start] = 0
    que.append(start)
    while que :
        now_conn = que.popleft()
        conn_connection = connection.get(now_conn)
        for next_con in conn_connection :
            if visited[next_con] != -1 :
                continue
            if next_con == end :
                return visited[now_conn] + 1
            visited[next_con] = visited[now_conn] + 1
            que.append(next_con)
    return visited[end]

print(bfs(start, end))
