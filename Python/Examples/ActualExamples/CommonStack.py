from collections import deque

class CommonStack:
    def __init__(self, n):
        self.stacks = [deque() for _ in range(n)]
        self.length = n
        self.result = []
        
    def process(self, queries):
        # query의 두 번째 값이 -1이면 pop, 아니면 push 연산 수행
        for query in queries:
            if query[1] == -1:
                self._pop(query)
            else:
                self._push(query)
            self.print_stacks(query)
        print(f"Result: {self.result}")
        return self.result
    
    def _check_all_empty(self):
        # 모두 비어있다면 True 반환
        if not any(self.stacks):
            return True
        return False
    
    def _push(self, query):
        # 만약 모든 스택이 비어있으면 중앙공간에 push
        if self._check_all_empty():
            for stack in self.stacks:
                stack.append(query[1])
        else:
            self.stacks[query[0] - 1].append(query[1])
    
    def _pop(self, query):
        # 중앙공간밖에 없는 경우
        if all(len(stack) == 1 for stack in self.stacks):
            for stack in self.stacks:
                popped_value = stack.pop()
            self.result.append(popped_value)
        # 바닥을 pop해야 하는 경우
        elif len(self.stacks[query[0] - 1]) == 1:
            popped_value = self.stacks[query[0] - 1][0]
            idx = self._find_nearest_stack_clockwise(query[0] - 1)
            self.stacks[idx].popleft()
            for i in range(self.length):
                if i != idx:
                    self.stacks[i][0] = self.stacks[idx][0]
            self.result.append(popped_value)
        # 빈 스택을 pop하려는 경우
        elif not self.stacks[query[0] - 1]:
            pass
        # 해당 스택의 바닥을 pop하지 않는 경우, 즉 스택의 크기가 2이상이면 그냥 pop
        else:
            popped_value = self.stacks[query[0] - 1].pop()
            self.result.append(popped_value)

    def _find_nearest_stack_clockwise(self, idx):
        for i in range(self.length):
            idx += 1
            if idx > self.length - 1:
                idx %= self.length
            
            if len(self.stacks[idx]) > 1:
                return idx

    def print_stacks(self, query):
        # 각 스택의 상태를 출력하는 함수
        print(f"Query: {query}")
        for i in range(self.length):
            print(f"Stack {i + 1}: {list(self.stacks[i])}")
        print("-" * 10)


def solution(n, queries):
    cs = CommonStack(n)
    cs.process(queries)
    return cs.result

if __name__ == "__main__":
    n = 3
    test_case = [[2, 3], [1, 2], [3, 4], [2, 5], [1, -1], [1, -1], [1, -1], [1, -1]]
    
    n = 6
    queries = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [3, 7], [4, 8], [5, 9], [6, 10], [4, 11], [5, 12], [6, 13], [5, 14], [6, 15], [6, 16], [1, -1], [2, -1], [3, -1], [3, -1], [4, -1], [5, -1], [6, -1]]
    
    result = solution(n, test_case)