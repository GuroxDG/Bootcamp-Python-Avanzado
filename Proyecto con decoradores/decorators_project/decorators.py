""" decorators functions """
import functools

from utils import authenticate

def authenticate_class(cls):
    """ Authenticate users """

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if authenticate(*args):
            return cls(*args, **kwargs)
        else:
            raise Exception('Unauthorized User')
        
    return wrapper
        