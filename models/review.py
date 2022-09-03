#!/usr/bin/python3
"""Define Review class which inherits the BaseModel class. """

from models.base_model import BaseModel


class Review(BaseModel):
    '''Representation of Review Class.'''

    place_id = ''
    user_id = ''
    text = ''
