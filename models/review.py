#!/usr/bin/python3
"""
Create Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ A Review class that inherits from the BaseModel class
    """
    place_id = ""
    user_id = ""
    text = ""
