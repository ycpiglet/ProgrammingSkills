import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees)
result = 0

while left <= right:
    mid = (left + right) // 2
    cut_sum = sum((tree - mid) for tree in trees if tree > mid)
    
    if cut_sum >= M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)