# %%

from toolz import *

def add(x, y):
    return x + y 

def sub(x, y):
    return x - y 

def mul(x, y):
    return x * y

def div(x, y):
    return x // y

def double(n):
    return n + n

print(functoolz.apply(double, 2))

print(double(2))

# %%

print('juxt')
juxt_funtion = functoolz.juxt(add, sub, mul, div)
print(juxt_funtion)
print(juxt_funtion(8, 100))


# %%

print('flip')
print(div(2, 6))
print(functoolz.flip(div, 2, 6))

# %%

print('Accumulate')
def add(x, y):
    print(f'{x=}, {y=}, result={x+y}')
    return x+y

print(list(itertoolz.accumulate(add, [8, 2, 3, 4])))
# entrega un iterador con los resultados de cada operación

# %%

print('Frecuencias')
fruit = ['banano', 'uva', 'fresa', 'banano', 'fresa', 'fresa']
print(itertoolz.frequencies(fruit))

# %%

print('Iterar sobre elemento no iterable')
def inc(x): return x + 10
counter = itertoolz.iterate(inc, 0)
print(next(counter))
print(next(counter))
print(next(counter))

# %%

print('Drop n cantidad de elementos')
print(list(itertoolz.drop(2, [10, 20, 30, 40, 50])))

# %%
