#!/usr/bin/python3
"""
This module define the class Place
"""
from .base_model import BaseModel


class Place(BaseModel):
    """
    This class define the Place entity
    """
    user_id = ""
    name = ""
    city_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0

    def __init__(self):
        super().__init__()
