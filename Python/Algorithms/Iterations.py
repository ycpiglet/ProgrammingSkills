import itertools

# generator이므로 iterable 객체가 생성됨, 즉 따로 형변환(Typecasting)을 해줘야 함
cartesian = list(itertools.product('ABCD', 'EF', 'GH'))
print(f'Cartesian Product: {cartesian}')

permutation = list(itertools.permutations('ABCD', 2))   # nPr
combination = list(itertools.combinations('ABCD', 2))   # nCr
permutation_w_replacement = list(itertools.product('ABCD', repeat=2))                   # n^r
combination_w_replacement = list(itertools.combinations_with_replacement('ABCD', 2))    # (n+r-1)Cr

print(f'Permutation: {permutation}')
print(f'Combination: {combination}')
print(f'Permutation with replacement: {permutation_w_replacement}')
print(f'Combination with replacement: {combination_w_replacement}')

count = itertools.count(start=10, step=1)
print(f'Count: ', end='')
for i in range(10):
    print(next(count), end=', ')
    if i == 9:
        print("")

cycle = itertools.cycle('ABCD')
print(f'Cycle: ', end='')
for i in range(10):
    print(next(cycle), end=', ')
    if i == 9:
        print("")
