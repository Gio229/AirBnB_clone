#!/usr/bin/python3
"""
This module define the Place
"""
import unittest

from ...models.user import User


class TestUser(unittest.TestCase):
    """
    This class define all tests for User
    """

    def test_instantiation(self):
        self.assertEqual(User, type(User()))


if __name__ == "__main__":
    unittest.main()
