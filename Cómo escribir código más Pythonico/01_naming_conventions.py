'''
Naming Conventions Examples
'''

# VARIABLES
# Not recommended
x = 'Maria Gomez'
y, z = x.split

# Recommended
name = 'Maria Gomez'
first_name, last_name = name.split()

# CONSTANTS
# Recommended
MAX_VALUE = 10
TOTAL = 30

# FUNCTIONS
# Not recommended


def db(x):
    return x * 2


# Recommended
def multiply_by_two(x):
    return x * 2

# CLASSES
# Recommended
class Person:

    # METHODS
    def get_name(self):
        return self.name
