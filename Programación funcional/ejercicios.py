# %% 

import itertools

## Iteradores Infinitos:

# %%

lp = [i for i in range(1, 100, 2)]
print(lp)

# %%

count_iter = itertools.count(start=1,step=2)
print(count_iter)
print(next(count_iter))
print('-----')

for i in count_iter:
    print(i)
    if i > 11:
        print(count_iter)
        break

print('-----')
print(next(count_iter))

# %%

nombres = ['Fatima', 'Edi', 'Jani']

cicly_iter = itertools.cycle(nombres)

print(next(cicly_iter))
print(next(cicly_iter))
print(next(cicly_iter))
print(next(cicly_iter))
print(next(cicly_iter))
print(next(cicly_iter))

# %%

nombres = ['Fatima', 'Edi', 'Jani']

cicly_iter = itertools.repeat(nombres, times = 5)

print(next(cicly_iter))
print(next(cicly_iter))
print(next(cicly_iter))
print(next(cicly_iter))
print(next(cicly_iter))
# 6 > 5 times 
print(next(cicly_iter)) # Error StopIteration

# %%

## Iteradores que terminan en la secuencia de entrada más corta:

accumulate_iter = itertools.accumulate([1, 2, 3, 4, 5, 6], lambda x,y: x + y)
print(list(accumulate_iter))
# [1, 3, 6, 10, 15, 21]

# %%

chain_iter = itertools.chain('ABCD', [1, 2, 3, 4])
print(list(chain_iter))
# ['A', 'B', 'C', 'D', 1, 2, 3, 4]

# %%

nombres = ['Camila', 'Ed', 'Jane', 'Fatima', 'Santiago', 'Juan']
mens = [0, 1, 0, 1, 1, 0]

compres_iter = itertools.compress(nombres, mens)
print(list(compres_iter))
# ['Ed', 'Fatima', 'Santiago']

# %%

elementos = itertools.groupby('AAAABBBCCCCDDAABBC')

#print(list(elementos))

parse_elementos = [[i[0],list(i[1])] for i in elementos]
print( parse_elementos )

# %%

## Iteradores combinatorios

producto = itertools.product('ABCD', 'xy')
print(list(producto))

producto = itertools.product(range(2), repeat=3)
print(list(producto))

# %%

nombres = ['Eduardo', 'Juani', 'Fatima']

print(f'Permutaciones de {nombres}')
permutaciones_iter = itertools.permutations(nombres)
print(list(permutaciones_iter))

# %%

print(f'Combinaciones de {nombres}')
permutaciones_iter = itertools.combinations(nombres, 2)
print(list(permutaciones_iter))

# %%

print(f'Combinaciones con elementos repetidos de {nombres}')
permutaciones_iter = itertools.combinations_with_replacement(nombres, 2)
print(list(permutaciones_iter))


# %%
