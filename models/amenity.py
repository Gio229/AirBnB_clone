#!/usr/bin/python3
"""
This module define the class Amenity
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    This class define the Amenity entity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
