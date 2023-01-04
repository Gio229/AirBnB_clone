#!/usr/bin/python3
"""
This module define the class State
"""
from base_model import BaseModel


class State(BaseModel):
    """
    This class define the State entity
    """
    name = ""

    def __init__(self):
        super().__init__()
