from collections import deque
import random

# FIFO 구조인 Queue는 deque 모듈 활용해야함
class Queue:
    # deque 객체로 대체
    def __init__(self):
        self.items = deque()
    
    # First In: 큐의 맨 앞에 데이터 삽입(Enqueue)
    def enqueue(self, item):
        self.items.append(item)
    
    # First Out: 큐의 맨 뒤의 데이터 제거(Dequeue)
    def dequeue(self):
        return self.items.popleft() if self.items else None
    
    # 큐가 비어있는지 확인(is_empty)
    def is_empty(self):
        return len(self.items) == 0
    
    # 큐의 크기 확인(Size)
    def size(self):
        return len(self.items)

queue = Queue()
N = 5
if queue.is_empty():
    for _ in range(N):
        queue.enqueue(random.randrange(1, 10))
        print(queue.items)

while not queue.is_empty():
    print(queue.dequeue(), queue.items)