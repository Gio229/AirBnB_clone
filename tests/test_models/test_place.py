#!/usr/bin/python3
"""
This module define the Place
"""
import unittest

from models.place import Place


class TestPlace(unittest.TestCase):
    """
    This class define all tests for Place
    """

    def test_instantiation(self):
        self.assertEqual(Place, type(Place()))


if __name__ == "__main__":
    unittest.main()
