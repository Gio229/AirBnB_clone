#!/usr/bin/python3
"""
This module define the class City
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    This class define the City entity
    """
    state_id = ""
    name = ""

    def __init__(self):
        super().__init__()
