from collections import deque

ex = [[1, 4], [1, 3], [2, 6], [3, -1], [1, 5], [2, -1]]
test_case = [[2, 3], [1, 4], [2, 5], [2, 6], [3, -1]]
N = 3

class newStack():
    def __init__(self, n):
        self.stacks = [deque() for _ in range(n)]
    
    def print(self):
        # print(f"Stacks: {self.stacks}")
        for i in range(len(self.stacks)):
            print(f"Stack {i + 1}: {list(self.stacks[i])}")
        print("-" * 10)
    
    def check(self, queries):
        for query in queries:
            if query[1] == -1:
                self.pop(query[0])
            else:
                self.push(query[0], query[1])
            self.print()
    
    def push(self, n, val):
        # 만약 전부 빈 스택이면 중앙 공간에 push
        if all(not stack for stack in self.stacks):
            for stack in self.stacks:
                stack.append(val)
            
        # 그게 아니라면 n번 스택에 push (index 주의할 것)
        else:
            self.stacks[n - 1].append(val)
    
    def pop(self, n):
        # n번째 스택의 크기가 1이라면, 즉 중앙공간밖에 없으면
        if len(self.stacks[n - 1]) == 1:
            for stack in self.stacks:
                if stack:
                    popped_value = stack.popleft()
            idx = n - 1
            while True:
                if idx + 1 > len(self.stacks) - 1:
                    idx -= len(self.stacks) - 1
                if self.stacks[idx + 1]:
                    for stack in self.stacks:
                        if not stack: # 중앙공간 처리: 스택이 비어있으면 푸시
                            stack.appendself.stacks[idx + 1][0]
                    return popped_value
                idx += 1
                    
        
        if self.stacks[n - 1]:
            popped_value = self.stacks[n - 1].pop()
            return popped_value

def solution(n, queries):
    stack = newStack(n)
    stack.check(queries)

if __name__ == "__main__":
    solution(N, ex)