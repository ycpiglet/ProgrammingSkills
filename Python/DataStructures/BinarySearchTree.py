import random
import sys
print(sys.getrecursionlimit())  # 현재 재귀 한도 출력
sys.setrecursionlimit(2000)     # 재귀 한도 설정 (권장하지 않음)

class Node:
    def __init__(self, data):
        self.data = data # 노드의 데이터 값
        self.left = None # 왼쪽 자식 노드를 가리킴
        self.right = None # 오른쪽 자식 노드를 가리킴

class BinarySearchTree:
    def __init__(self):
        self.root = None # 트리의 루트 노드
    
    # 이진 트리에 새로운 노드를 삽입하는 함수(BST 방식)
    def insert(self, data):
        new_node = Node(data)
        
        # 루트 노드가 없으면 새로운 노드를 루트로 설정
        if self.root is None:
            self.root = new_node
        else:
            # 루트 노드부터 재귀적으로 노드를 삽입
            self._insert_recursive(self.root, new_node)
    
    # 재귀적으로 삽입 위치를 찾아주는 함수
    def _insert_recursive(self, current, new_node):
        # 삽입할 노드가 현재 노드보다 작을 경우 왼쪽으로 이동
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        #삽입할 노드가 현재 노드보다 크거나 같을 경우 오른쪽으로 이동
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)
    
    # 이진 트리에서 값을 검색하는 함수
    def search(self, data):
        return self._search_recursive(self.root, data)
    
    # 재귀적으로 노드를 검색하는 함수
    def _search_recursive(self, current, data):
        # 현재 노드가 None이면, 값이 트리에 존재하지 않음
        if current is None:
            return None
        
        # 찾는 값이 현재 노드의 데이터와 일치할 경우
        if current.data == data:
            return current
        
        # 찾는 값이 더 작으면 왼쪽으로 탐색
        elif data < current.data:
            return self._search_recursive(current.left, data)
        
        # 찾는 값이 더 크거나 같으면 오른쪽으로 탐색
        else:
            return self._search_recursive(current.right, data)
    
    # 이진 트리를 순회하는 함수(중위 순회)
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    # 중위 순회를 재귀적으로 구현한 함수
    def _inorder_recursive(self, current, result):
        if current is not None:
            self._inorder_recursive(current.left, result)
            result.append(current.data)
            self._inorder_recursive(current.right, result)
            
    
    def preorder_traversal(self):
        pass
    
    def _preorder_recursive(self, current, result):
        pass
    
    def postorder_traversal(self):
        pass
    
    def _postorder_traversal(self, current, result):
        pass
    
    def delete(self, data):
        pass
    
    def _delete_recursive(self, current, data):
        pass
    
    def _find_min(self, node):
        pass

# 이진 트리 생성
tree = BinarySearchTree()

# 입력 값 생성하기
N = 10
items = random.sample(range(100), N)

# 노드 삽입
for i in range(N):
    tree.insert(items[i])

# 트리 순회(중위 순회)
print(tree.inorder_traversal())

# 트리에서 특정 값을 검색
search_result = tree.search(3)
if search_result:
    print(f'찾은 노드: {search_result.data}')
else:
    print('값이 트리에 존재하지 않습니다.')