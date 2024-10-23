import unittest, random
from CommonStack import solution

class TestSharedBottomStack(unittest.TestCase):
    # 기본 케이스
    def test_case_1(self):
        n = 3
        queries = [[2, 3], [1, 2], [3, 4], [2, 5], [1, -1], [1, -1], [1, -1], [1, -1]]
        result = solution(n, queries)
        self.assertEqual(result, [2, 3, 5, 4])
    
    # 모든 스택이 비어 있는 경우
    def test_case_2(self):
        n = 9
        queries = [[1, 1], [1, -1], [2, -1]]
        result = solution(n, queries)
        self.assertEqual(result, [1])
    
    # push, pop 반복
    def test_case_3(self):
        n = 5
        queries = [[1, 1], [1, -1], [4, 3], [2, -1], [3, 5], [3, -1], [5, 7], [5, -1], [2, 9], [4, -1]]
        result = solution(n, queries)
        self.assertEqual(result, [1, 3, 5, 7, 9])
    
    # 여러 번의 연속된 pop
    def test_case_4(self):
        n = 7
        queries = [[1, 1], [1, 2], [2, 3], [3, 4], [1, -1], [2, -1], [3, -1]]
        result = solution(n, queries)
        self.assertEqual(result, [2, 3, 4])
    
    # 여러 스택에서 push 및 pop
    def test_case_5(self):
        n = 15
        queries = [[1, 1], [2, 2], [3, 3], [1, -1], [2, -1], [3, -1]]
        result = solution(n, queries)
        self.assertEqual(result, [1, 2, 3])
    
    # 많은 연산
    def test_caset_6(self):
        n = 30
        queries = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [3, 7], [4, 8], [5, 9], [6, 10], [4, 11], [5, 12], [6, 13], [5, 14], [6, 15], [6, 16], [1, -1], [2, -1], [3, -1], [3, -1], [4, -1], [5, -1], [6, -1]]
        result = solution(n, queries)
        self.assertEqual(result, [1, 2, 7, 3, 11, 14, 16])
    
    def test_case_7(self):
        n = 1
        queries = [[1, 3], [1, -1], [1, 2], [1, 6], [1, -1], [1, 13], [1, -1], [1, -1], [1, 9], [1, -1]]
        result = solution(n, queries)
        self.assertEqual(result, [3, 6, 13, 2, 9])
    
    # def test_case_8(self):
    #     n = random.randrange(1, 100)
    #     num_op = random.randrange(1, 100)
    #     queries = self.generate_random_test_case(n, num_op)
    #     result = solution(n, queries)
    #     self.assertEqual(result, [])
    
    # def generate_random_test_case(self, num_stacks, num_operations):
    #     queries = []
    #     for _ in range(num_operations):
    #         stack_index = random.randint(1, num_stacks)  # 스택 인덱스 선택 (1 ~ num_stacks)
    #         operation = random.choice([-1, random.randint(1, 100)])  # -1이면 pop, 아니면 push할 값
    #         queries.append([stack_index, operation])
    #     return queries

if __name__ == "__main__":
    unittest.main()
