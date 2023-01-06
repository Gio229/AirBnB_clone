#!/usr/bin/python3
"""
This module define the TestCity
"""
import unittest

from models.city import City


class TestCity(unittest.TestCase):
    """
    This class define all tests for City
    """

    def test_instantiation(self):
        self.assertEqual(City, type(City()))


if __name__ == "__main__":
    unittest.main()
