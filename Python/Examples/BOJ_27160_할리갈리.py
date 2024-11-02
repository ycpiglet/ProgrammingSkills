import sys
input = sys.stdin.readline

# 과일 종류와 초기 개수
fruits = {"STRAWBERRY": 0, "BANANA": 0, "LIME": 0, "PLUM": 0}

# 입력 개수
N = int(input())

for _ in range(N):
    fruit, num = input().split()
    fruits[fruit] += int(num)

# 5가 존재하는지 확인
if 5 in fruits.values():
    print("YES")
else:
    print("NO")