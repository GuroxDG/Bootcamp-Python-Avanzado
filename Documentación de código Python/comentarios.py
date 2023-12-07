'''
Comentarios
'''

def hello_world():
    # una simple función que imprime un saludo
    # TODO: incluir nombre de usuario
    print('Hello world')


print(hello_world.__doc__)

def hello_world_2():
    """ Esto sigue siendo una función"""
    print('Hello world')
    
print(hello_world_2.__doc__)


def some_function(argument):
    """Summary or Description of the function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    float: Returning value
    
    """
    return float(argument)

print(some_function.__doc__)
help(some_function)


class MyClass:
    """ Este es el docstring de la clase"""

    def __init__(self):
        """Este es el docstring del inicializador"""
        pass

    def hello(self):
        """Este es el docstring del método de clase"""
        pass

# Google Style

def add(a, b):
    """This function calculate the sum

    Args:
        a (int): the first number
        b (int): the first number

    Returns:
        float: The sum of two numbers

    """
    
    return float(a + b)


# reStructuredText Style

def add(a, b):
    """
    This function calculate the sum

    :param a: the first number
    :type a: int or float
    :param b: the first number
    :type b: int or float
    :return: The sum of two numbers
    :rtype: float

    """
    
    return float(a + b)