#!/usr/bin/python3
"""
This module define the Place
"""
import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    This class define all tests for Amenity
    """

    def test_instantiation(self):
        self.assertEqual(Amenity, type(Amenity()))


if __name__ == "__main__":
    unittest.main()
