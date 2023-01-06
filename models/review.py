#!/usr/bin/python3
"""
This module define the class Review
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    This class define the Review entity
    """
    user_id = ""
    place_id = ""
    text = ""

    def __init__(self):
        super().__init__()
