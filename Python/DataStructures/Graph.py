from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        
        # 인접한 노드를 큐에 넣고 방문 처리
        for next_node in graph[node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

# 인접 리스트로 표현된 그래프
graph = [
    [],          # 0번 노드는 사용하지 않음
    [2, 3, 8],   # 1번 노드와 연결된 노드들
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 처리 배열
visited = [False] * 9

# 1번 노드에서 BFS 시작
bfs(graph, 1, visited)


def dfs(graph, start, visited):
    # 현재 노드를 방문 처리
    visited[start] = True
    print(start, end=' ')

    # 인접한 노드를 방문
    for next_node in graph[start]:
        if not visited[next_node]:
            dfs(graph, next_node, visited)

# 인접 리스트로 표현된 그래프
graph = [
    [],          # 0번 노드는 사용하지 않음
    [2, 3, 8],   # 1번 노드와 연결된 노드들
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 처리 배열
visited = [False] * 9

# 1번 노드에서 DFS 시작
dfs(graph, 1, visited)
