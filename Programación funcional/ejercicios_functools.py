# %% 

import functools

# @cache
# @lru_cache
# objects -> @cached_property

# %%
#@functools.cache
@functools.lru_cache(maxsize=5)
def factorial(n):
    print(f'Llamado de la función con valor {n}')
    if n == 1:
        print(f'Resultado de la función {n} = {1}')
        return 1
    x = n * factorial(n-1)
    print(f'Resultado de la función valor {n} = {x}')
    return x

print(factorial(10))
# %%
print(factorial(10))

# %%
print(factorial(5))

# %%
print(factorial(11))
# %%

print(factorial.cache_info())
# factorial.cache_clear
# factorial.cache_parameters

# %%

def multiply(x, y):
    return x * y

multiply_by_10 = functools.partial(multiply,10)
multiply_by_2 = functools.partial(multiply,2)


print(multiply(10,8))
print(multiply_by_10(8))
print(multiply(2,8))
print(multiply_by_2(8))

# %%

def add(a, b):
    print(f'{a=}, {b=}. result={a+b}')
    return a + b

data_list = [1, 2, 3, 4, 5, 6, 7]
result = functools.reduce(add, data_list)
print(result)

# %%

from functools import singledispatch

@singledispatch
def add_(a, b):
    raise NotImplementedError('Unsuported type')

@add_.register(int)
def _(a, b):
    return a + b

@add_.register(list)
def _(a, b):
    print('Type list')
    return sum(a) + sum(b)

print(add_(1, 10))
print(add_([3, 4, 5], [6, 5, 7]))
print(add_({1, 23}, {4, 5}))


# %%
