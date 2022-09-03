#!/usr/bin/python3
""" Define User class which inherits the BaseModel class. """

from models.base_model import BaseModel


class User(BaseModel):
    '''User Class Definition.'''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
