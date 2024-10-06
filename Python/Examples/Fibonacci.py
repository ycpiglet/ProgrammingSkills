import sys
sys.setrecursionlimit(10 ** 6)

class Fibonacci:
    def __init__(self):
        self.memo = {}  # 메모이제이션을 위한 딕셔너리

    def calculate(self, n):
        # 이미 계산된 값이 있으면 반환
        if n in self.memo:
            return self.memo[n]
        # 기저 조건: n이 0 또는 1일 때
        if n <= 1:
            self.memo[n] = n
        else:
            # 재귀적으로 피보나치 계산하고 저장
            self.memo[n] = self.calculate(n - 2) + self.calculate(n - 1)
        return self.memo[n]

if __name__ == '__main__':
    fibonacci = Fibonacci()
    print(fibonacci.calculate(10))  # 10번째 피보나치 수 계산
    print(fibonacci.memo.values())