from collections import deque

def wulrus_operator():
    print("True!!") if (a := 3) else print("False!!")

    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 0]

    for x, y in zip(a, b):
        print(x+y)

l = [1, 2, 3, 4, 5]
print(max(l))

q = deque(l)
print(max(l))

print(l[-2])