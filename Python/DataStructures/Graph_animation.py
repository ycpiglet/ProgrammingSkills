import matplotlib.pyplot as plt
import networkx as nx
import time
from collections import deque

# 더 복잡한 트리 구조 생성
G = nx.DiGraph()
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (4, 9), (5, 10), (6, 11), (7, 12), (7, 13)]
G.add_edges_from(edges)

# 계층적 노드 위치 설정 (수직 계층형)
pos = {1: (0, 4), 2: (-1.5, 3), 3: (1.5, 3), 4: (-2, 2), 5: (-1, 2), 6: (1, 2), 7: (2, 2),
       8: (-2.5, 1), 9: (-1.5, 1), 10: (-0.5, 1), 11: (1, 1), 12: (1.5, 1), 13: (2.5, 1)}

# DFS 함수 (스택 사용)
def dfs(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            yield node, list(stack)  # 방문한 노드와 스택 상태 전달
            stack.extend(sorted(graph[node], reverse=True))

# BFS 함수 (큐 사용)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            yield node, list(queue)  # 방문한 노드와 큐 상태 전달
            queue.extend(sorted(graph[node]))

# 스택 (배터리 아이콘 형태) 시각화 함수
def visualize_stack(stack_state, ax):
    ax.clear()
    ax.set_title("Stack (LIFO)", pad=20)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 10)
    ax.axis('off')  # 축을 제거하여 깔끔하게
    
    for i, elem in enumerate(stack_state):
        ax.bar(0.5, 1, bottom=i, color='gray', edgecolor='black', align='center')
        ax.text(0.5, i + 0.5, str(elem), ha='center', va='center', color='white')

# 큐 (수평형태) 시각화 함수
def visualize_queue(queue_state, ax):
    ax.clear()
    ax.set_title("Queue (FIFO)", pad=20)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    ax.axis('off')  # 축을 제거하여 깔끔하게
    
    for i, elem in enumerate(queue_state):
        ax.barh(0.5, 1, left=i, color='lightblue', edgecolor='black', align='center')
        ax.text(i + 0.5, 0.5, str(elem), ha='center', va='center', color='black')

# 탐색 애니메이션 시각화 함수
def visualize_search(search_func, is_stack=True):
    plt.ion()  # interactive mode on
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 6))
    
    # 처음에 트리 전체를 그리기 (계층적 구조)
    nx.draw(G, pos, ax=ax1, with_labels=True, node_color="lightgreen", node_size=500, font_size=10)
    ax1.set_title("Tree Structure", pad=20)
    
    # 탐색 진행하면서 시각화 업데이트
    for node, state in search_func(G, 1):
        # 트리에서 노드 빨간색으로 변경하여 방문 표시
        nx.draw_networkx_nodes(G, pos, ax=ax1, nodelist=[node], node_color="red", node_size=500)
        
        # 스택/큐 시각화
        if is_stack:
            visualize_stack(state, ax2)  # 스택 시각화
        else:
            visualize_queue(state, ax3)  # 큐 시각화
        
        plt.draw()
        plt.pause(1)  # 1초간 대기 (애니메이션 효과)
    
    plt.ioff()  # interactive mode off
    plt.show()

# DFS 실행 (스택: 세로형)
visualize_search(dfs, is_stack=True)

# BFS 실행 (큐: 가로형)
visualize_search(bfs, is_stack=False)
