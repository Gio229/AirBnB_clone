#!/usr/bin/python3
"""
This module define the TestCity
"""
from datetime import datetime
import unittest

from models.city import City


class TestCity(unittest.TestCase):
    """
    This class define all tests for City
    """

    def test_instantiation(self):
        city = City()
        self.assertEqual(City, type(city))
        self.assertTrue(type(city.id) is str)
        self.assertTrue(type(city.created_at) is datetime)
        self.assertTrue(type(city.updated_at) is datetime)

    def test_name(self):
        """Test if name attribute is string
        """
        self.assertEqual(str, type(City.name))
    
    def test_state_id(self):
        """Test if state_id attribute is string
        """
        self.assertEqual(str, type(City.state_id))

if __name__ == "__main__":
    unittest.main()
