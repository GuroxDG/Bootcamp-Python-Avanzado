'''
Programming Recomendations
'''

## Dont compare Boolean values to True or False
## using the equivalent operador

# Not recomended
my_bool = 6 > 5
if my_bool == True:
    print('6 is bigger than 5')

# Recomended
if my_bool:
    print('6 is bigger than 5')

## Use the fact that empty sequences are false in if statements

# Not recomended
my_list = []
my_string = ''
if not len(my_list):
    print('List is empty')

# Recomended
my_list = []
if not my_list:
    print('Lisst is empty')

## Use is not rather than not ... is in if statements

# Not recommended
if not x is None:
    print('x exists')

# Recommended
if x is not None:
    print('x exists')

## Dont use if x: when you mean if x is not None

# Not Recommended
if arg:
    # Do something with arg...
    pass

# Recommended
if arg is not None:
    # Do something with arg...
    pass

## Use . startswith() and .endswith()

word = 'mycat'

# Not recommended
if word[:3] == 'cat':
    print('The word starts with "cat"')

# Recommended
if word.startswith('cat'):
    print('The word starts with "cat"')