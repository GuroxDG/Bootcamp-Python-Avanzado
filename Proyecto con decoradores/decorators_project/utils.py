""" Utils functions """
import csv
import os
import re

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
    
def is_valid_password(pwd: str) -> bool:
    """
    Checks if the inputted password follows the next conditions:
    - At least 8 characters
    - Must be restricted to, though does not specifically require any of:
        - uppercase letters: A-Z
        - lowercase letters: a-z
        - numbers: 0-9
        - any of the special characters: @#$%^&+=
    :param pwd: string
    :return: boolean
    """
    if re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", pwd):
        return True
    else:
        return False