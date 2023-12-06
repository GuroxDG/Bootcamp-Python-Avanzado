"""
Whitespaces
"""

def function(default_parameter=5):
    pass

## Assignations
x = 3
y = 2

## Priority
# Not Recommended
if x>5 and x%2==0:
    print('x is larger than 5 and ...')

# Recommended
if x > 5 and x % 2 == 0:
    print('x is larger than 5 and ...')

# Definitely do not do this
if x >5 and x% 2== 0:
    print('x is larger than 5 and ...')

## Operations
# Recommended
y = x**2 + 5
z = (x+y) * (x-y)

# Not Recommended
y = x ** 2 + 5
z = (x + y) * (x - y)

## Lists
list[3:4]

#Treat the colon as the operator with lowest priority
list[x+1 : x+2]

# In an extended slice, both colons must be
# surrounded by the same amount of whitespace
list[3:4:5] #😒
list[x+1 : x+2 : x+3] #😊

# The space is ommited if slice parameter is ommited
list[x+1 : x+2 :]
