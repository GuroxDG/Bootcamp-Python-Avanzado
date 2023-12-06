'''
Comments and Docstring
'''

def quadratic(a, b, c, x):
    # Calculate the solution to a quadratric equation
    # using the quadratic formula
    #
    # There are always two solutions to a quadratic equation, x_1 and x_2
    x_1 = ( - b +(b**2 -4*a*c)**(1/2)) / (2*a)
    x_2 = ( - b -(b**2 -4*a*c)**(1/2)) / (2*a)
    return x_1, x_2

x = 5 # This is an inline comment

def quadratic(a, b, c, x):
    """Solve quadratic equation via the quadratic formula.

    A quadratic equation has the following form:
    ax**2 + bx + c = 0

    There always two solutions to a quadratic equation: x_1 & x_2.
    :return:
    """
    x_1 = ( - b +(b**2 -4*a*c)**(1/2)) / (2*a)
    x_2 = ( - b -(b**2 -4*a*c)**(1/2)) / (2*a)
    return x_1, x_2


def quadratic(a, b, c, x):
    """Use the quadratic formula"""
    x_1 = ( - b +(b**2 -4*a*c)**(1/2)) / (2*a)
    x_2 = ( - b -(b**2 -4*a*c)**(1/2)) / (2*a)
    return x_1, x_2
