import random

# LIFO 구조인 Stack은 List(동적 배열) 자료형으로 대체 가능
class Stack():
    # 스택을 빈 리스트로 초기화
    def __init__(self) -> None:
        self.items = list()
        print("Stack is created!!")
        print(f'Stack: {self.items}')
    
    # First In: 스택의 맨 위에 값을 넣는 메소드(Push)
    def push(self, item):
        self.items.append(item)
    
    # Last Out: 스택의 맨 위에서 값을 빼는 메소드(Pop)
    def pop(self):
        return self.items.pop() if self.items else None
    
    # 스택의 가장 위에 있는 값 확인(Peak)
    def peek(self):
        return self.items[-1] if self.items else None
    
    # 스택이 비었는지 확인(is_empty)
    def is_empty(self):
        return len(self.items) == 0
    
    # 스택의 크기 확인(Size)
    def size(self):
        return len(self.items)
    
my_stack = Stack()
N = 5
numbers = list(range(10))

if my_stack.is_empty():
    for _ in range(5):
        random_val = random.choice(numbers)
        numbers.remove(random_val)
        my_stack.push(random_val)
        print(f'Stack: {my_stack.items}, Push: {random_val}')
        
for _ in range(5):
    popped_value = my_stack.pop()
    print(f'Stack: {my_stack.items}, Pop: {popped_value}')
    if my_stack.is_empty():
        print("Stack is empty!!")