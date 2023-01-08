#!/usr/bin/python3
"""
This module define the Place
"""
from datetime import datetime
import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    This class define all tests for Amenity
    """

    def test_instantiation(self):
        amenity = Amenity()
        self.assertEqual(Amenity, type(amenity))
        self.assertTrue(type(amenity.id) is str)
        self.assertTrue(type(amenity.created_at) is datetime)
        self.assertTrue(type(amenity.updated_at) is datetime)
    
    def test_name(self):
        """Test if name attribute is string
        """
        self.assertEqual(str, type(Amenity.name))


if __name__ == "__main__":
    unittest.main()
