'''
Identation
'''

arg_one, arg_two, arg_three, arg_four = (1, 2, 3, 4)

# Line Breaks
# Function definition
def function(arg_one, arg_two, 
             arg_three, 
             arg_four):
    return arg_one, arg_two, arg_three, arg_four


# Call function
# Recommended
var = function(
    arg_one, arg_two, 
    arg_three, arg_four)

var = function(arg_one, arg_two, 
               arg_three, arg_four)

# Not Recommended
var = function(arg_one, arg_two,
     arg_three, arg_four)


# Break Lines
x = 5
if (x < 3
        and x > 0):
    pass

lsit_number = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
]

from libs import (lib1, 
                  lib2, lib3)
 