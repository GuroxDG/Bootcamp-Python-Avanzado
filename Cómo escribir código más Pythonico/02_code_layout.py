'''
Code Layout
'''

# BLANK LINES
# Surround top-level functions and classes with simple blank line


class MyFirstClass:
    # Surround method definitions inside classes with a single blank line.
    def first_methos(self):
        return None
    
    def second_method(self):
        return None
    

class MySecondClass:
    pass


def top_level_function():
    return None


# Use blank lines sparingly inside functions to show clear steps
def calculate_variance(number_list):
    sum_list = 0
    for number in number_list:
        sum_list = sum_list + number
    mean = sum_list / len(number_list)

    sum_squares = 0
    for number in number_list:
        sum_squares = sum_squares + number**2
    mean_squares = sum_squares / len(number_list)

    return mean_squares - mean**2


# Maximun Line Length ans Line Breaking
# functions
def long_function(
        argument_one, argument_two, argument_one_three, argument_four):
    return argument_one

def long_function(argument_one, argument_two, 
                  argument_one_three, argument_four):
    return argument_one

