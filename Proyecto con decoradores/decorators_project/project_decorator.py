""" Project to run decorators """
from decorators import authenticate_class

@authenticate_class
class MyClass:
    """ Main class"""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def say_hello(self):
        """ Say Hello"""
        print(f'Hi {self.username}, welcome to our system!')

    def show_password(self):
        """ Show password """
        print(f'Hi {self.username}, your password starts by: {self.password[:4]}{len(self.password[4:])*"*"}')



my_class = MyClass('gustavo', '123')
print(my_class.username)
print(my_class.password)
my_class.say_hello()
my_class.show_password()
