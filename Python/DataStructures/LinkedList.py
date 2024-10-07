class Node:
    def __init__(self, data):
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드를 가리키는 데이터

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None # 링크드 리스트의 첫 노드를 가리키는 포인터
    
    # 링크드 리스트 끝에 노드 추가(Append)
    def append(self, data):
        new_node = Node(data) # 새로운 노드 생성
        if not self.head: # 링크드 리스트가 비어있을 때
            self.head = new_node # 새로운 노드를 첫 노드로 설정
            return
        last = self.head
        while last.next: # 마지막 노드까지 이동
            last = last.next
        last.next = new_node # 마지막 노드의 다음 포인터에 새 노드 연결
    
    # 링크드 리스트 출력(Traverse)
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None") # 마지막 노드 표시
    
    # 링크드 리스트 데이터 검색(Search)
    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current # 데이터가 포함된 노드 반환
            else:
                current = current.next
        return None # 데이터가 없으면 None 반환
    
    # 링크드 리스트 중간에 노드 추가(Insert)
    def insert(self, prev_node, data):
        if not prev_node:
            print("이전 노드가 없습니다.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    # 링크드 리스트 노드 삭제(Delete)
    def delete(self, key):
        current = self.head
        prev = None
        
        # 삭제할 노드가 head인 경우
        if current and current.data == key:
            self.head = current.next # head를 다음 노드로 이동
            current = None
            return
        
        # 삭제할 노드를 탐색
        while current and current.data != key:
            prev = current
            current = current.next
        
        # 삭제할 노드가 없으면 종료
        if current is None:
            return
        
        # 이전 노드가 현재 노드의 다음 노드를 가리키도록 변경
        prev.next = current.next
        current = None
        
    def delete_last(self):
        if self.head is None:
            return  # 리스트가 비어 있으면 아무 작업도 하지 않음
        
        # 리스트에 노드가 하나밖에 없는 경우
        if self.head.next is None:
            self.head = None
            return
        
        # 마지막 노드 탐색
        current = self.head
        while current.next.next is not None:
            current = current.next
        
        # 마지막 노드 삭제
        current.next = None
    
    # 첫 번째 노드 삭제
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
        
        # head를 다음 노드로 옮김
        self.head = self.head.next
    
    # 링크드 리스트의 첫 번째 노드 확인(Peek)
    def peek(self):
        if self.head is None:
            return None # 링크드 리스트가 비어있으면 None 반환
        return self.head.data
    
    # 링크드 리스트가 비어있는지 확인(is_empty)
    def is_empty(self):
        return self.head is None

class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 중간 노드 삭제
    def delete_node(self, key):
        current = self.head
        
        # 삭제할 노드 탐색
        while current is not None and current.data != key:
            current = current.next
        
        # 노드가 없으면 종료
        if current is None:
            return
        
        # 삭제할 노드가 첫 번째 노드인 경우
        if current == self.head:
            self.head = current.next
            if self.head is not None:
                self.head.prev = None
            return
        
        # 삭제할 노드가 중간 또는 마지막 노드인 경우
        if current.next is not None:
            current.next.prev = current.prev
        
        if current.prev is not None:
            current.prev.next = current.next
        
        current = None

# 링크드 리스트 생성
llist = SinglyLinkedList()

# 노드 추가
llist.append("바나나")
llist.append("사과")
llist.append("복숭아")

# 링크드 리스트 출력
llist.print_list()

# 링크드 리스트 첫 번째 노드 출력
print(f'첫 번쨰 노드: {llist.peek()}')

# 데이터 검색
data = "사과"
node = llist.search(data)
# 메소드는 결과를 반환만 하고, 실제 출력은 호출하는 쪽에서 구현하는 것이 더욱 유연함
if node:
    print(f'데이터 [{data}]가 존재합니다.')
else:
    print("해당 데이터가 없습니다.")

# 링크드 리스트 중간에(다음 노드에) 노드 추가
llist.insert(node, "수박")
llist.print_list()

# 링크드 리스트 노드 삭제
# item = llist.search("사과")
llist.delete("사과")
llist.print_list()