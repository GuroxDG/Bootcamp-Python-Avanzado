'''
Generators
'''

# Muy útiles con las listas de valores infinitos
# Entre llamado y llamdo, el objeto iterable entra
# en un estado de pausa (suspención)

# Generic Example
def generator_function(sequence):
    for x in sequence:
        yield x

# Pair Numbers
def pair_numbers():
    for x in range(0, 102, 2):
        yield x

if __name__ == '__main__':
    generator_pairs = pair_numbers()

    while True:
        try:
            print(next(generator_pairs))
        except StopIteration:
            print('No existen más pares del 0 al 100')
            break

    print('Generator Function')
    data_list = [1, 2, 3, 5, 6, 6,]
    gen_fn = generator_function(data_list)

    print(next(gen_fn))
    print(next(gen_fn))
    print(next(gen_fn))
    print(next(gen_fn))
    print(next(gen_fn))