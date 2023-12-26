""" Utils functions """
import csv
import os

def get_users(file_name):
    """ get users """
    with open(f'{os.path.dirname(__file__)}/{file_name}','r',encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    return data

def authenticate(username, password):
    """ Validate users """
    user = {
        "username" : username,
        "password" : password
    }
    
    print(user)
    dict_users = get_users('users.csv')
    print(dict_users)

    if user in dict_users:
        return True
    else:
        return False