import math

def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    return n * factorial_recursive(n-1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def permutation(n, r):
    return factorial_iterative(n) // factorial_iterative(n - r)

def combination(n, r):
    return factorial_iterative(n) // (factorial_iterative(r) * factorial_iterative(n - r))

def permutation_without_factorial(n, r):
    result = 1
    for i in range(n, n - r, -1):
        result *= i
    return result

def combination_without_factorial(n, r):
    if r > n - r:  # 조합에서 r과 n-r 중 더 작은 값으로 계산하는 것이 효율적
        r = n - r
    result = 1
    for i in range(r):
        result *= (n - i)
        result //= (i + 1)
    return result

f = math.factorial(5)
p = math.perm(5, 3)
c = math.comb(5, 3)

print(f, p, c)