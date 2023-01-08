#!/usr/bin/python3
"""
This module define the Place
"""
from datetime import datetime
import unittest

from models.place import Place


class TestPlace(unittest.TestCase):
    """
    This class define all tests for Place
    """

    def test_instantiation(self):
        place = Place()
        self.assertEqual(Place, type(place))
        self.assertTrue(type(place.id) is str)
        self.assertTrue(type(place.created_at) is datetime)
        self.assertTrue(type(place.updated_at) is datetime)
    
    def test_name(self):
        """Test if name attribute is string
        """
        self.assertEqual(str, type(Place.name))

    def test_city_id(self):
        """Test if city_id attribute is string
        """
        self.assertEqual(type(Place.city_id), str)
    
    def test_user_id(self):
        """Test if user_id attribute is string
        """
        self.assertEqual(type(Place.user_id), str)
    
    def test_description(self):
        """Test if description attribute is string
        """
        self.assertEqual(type(Place.description), str)
    
    def test_number_rooms(self):
        """Test if number_rooms attribute is integer
        """
        self.assertEqual(type(Place.number_rooms), int)
    
    def test_number_bathrooms(self):
        """Test if number_bathrooms attribute is integer
        """
        self.assertEqual(type(Place.number_bathrooms), int)
    
    def test_max_guest(self):
        """Test if max_guest attribute is string
        """
        self.assertEqual(type(Place.max_guest), int)
    
    def test_price_by_night(self):
        """Test if price_by_night attribute is integer
        """
        self.assertEqual(type(Place.price_by_night), int)
    
    def test_latitude(self):
        """Test if latitude attribute is float
        """
        self.assertEqual(type(Place.latitude), float)
    
    def test_longitude(self):
        """Test if longitude attribute is float
        """
        self.assertEqual(type(Place.longitude), float)
    
    def test_amenity_ids(self):
        """Test if name attribute is string
        """
        self.assertEqual(type(Place.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
