import time
import sys
sys.setrecursionlimit(2000)

def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    return n * factorial_recursive(n-1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

start = time.time()
result = factorial_recursive(1000)
end = time.time()

print(f'Recursive: {end - start}')

start = time.time()
result = factorial_iterative(1000)
end = time.time()

print(f'Iterative: {end - start}')
