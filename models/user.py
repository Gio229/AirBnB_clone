#!/usr/bin/python3
"""
This module define the class User
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    This class define the User entity
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
