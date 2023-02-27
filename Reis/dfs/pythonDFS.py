from collections import deque


def dfs(graph, start_node) :
    need_visited, visited = list(), list()

    need_visited.append(start_node)

    while need_visited :
        node = need_visited.pop(); # 가장 마지막 데이터 추출 -> list에서 pop() 활용하면 성능에서 떨어진다.
        if node not in visited :
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

def dfs2(graph, start_node) :
    visited = list()
    need_visited = deque() # -> dq 활용 방식
    need_visited.append(start_node)

    while need_visited :
        node = need_visited.pop() # -> 성능이 deque가 더 좋대
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

def dfs3(graph, start_node, visited = []) :
    visited.append(start_node)
    for node in graph[start_node]:
        if node not in visited:
            dfs3(graph, node, visited)
    return visited